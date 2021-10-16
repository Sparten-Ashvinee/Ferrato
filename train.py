import time
import argparse
import numpy as np
import copy
import torch
import torch.nn.functional as F
import torch.optim as optim
from torch.optim import lr_scheduler
from utils import load_data, accuracy
from models import GCN
from onnix_food import export_onnix, ColaPredictor
import wandb
import os
import hydra
from omegaconf import OmegaConf



run = wandb.init(project="Ferrato", tags=["GNN-food"])

os.environ["WANDB_NOTEBOOK_NAME"] = "food_gnn_notebook"
path = '/home/ashvinee/Documents/Ferrato/'


def check_cuda(cfg):
    np.random.seed(cfg.training.seed)
    torch.manual_seed(cfg.training.seed)
    #cfg.training.cuda = not cfg.processing.no_cuda and torch.cuda.is_available()
    if cfg.training.cuda:
        torch.cuda.manual_seed(cfg.training.seed)



def imp_cuda(cfg, model, adj, features, labels, idx_train, idx_val, idx_test):
    if cfg.training.cuda:
        model.cuda()
        features = features.cuda()
        adj = adj.cuda()
        labels = labels.cuda()
        idx_train = idx_train.cuda()
        idx_val = idx_val.cuda()
        idx_test = idx_test.cuda()


def test(model, adj, features, labels, idx_test):
    model.eval()
    output = model(features, adj)
    loss_test = F.nll_loss(output[idx_test[:354]], labels[idx_test[:354]])
    acc_test = accuracy(output[idx_test[:354]], labels[idx_test[:354]])

    wandb.log({"loss_test": loss_test.item()})
    wandb.log({"acc_test": acc_test.item()})

    print("Test set results:",
          "loss= {:.4f}".format(loss_test.item()),
          "accuracy= {:.4f}".format(acc_test.item()))


# Train model
def train(cfg, model, optimizer, scheduler, adj, features, labels, idx_train, idx_val):
    t_total = time.time()
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    for epoch in range(cfg.training.epochs):
        #train(epoch)
        t = time.time()
        model.train()
        optimizer.zero_grad()
        output = model(features, adj)
        loss_train = F.nll_loss(output[idx_train], labels[idx_train])
        acc_train = accuracy(output[idx_train], labels[idx_train])
        loss_train.backward()
        optimizer.step()
        #scheduler.step()
        if not cfg.training.fastmode:
            # Evaluate validation set performance separately,
            # deactivates dropout during validation run.
            model.eval()
            output = model(features, adj)

        loss_val = F.nll_loss(output[idx_val], labels[idx_val])
        acc_val = accuracy(output[idx_val], labels[idx_val])

        if acc_val > best_acc:
            best_acc = acc_val
            best_model_wts = copy.deepcopy(model.state_dict())

        wandb.log({"loss_train": loss_train.item()})
        wandb.log({"acc_train": acc_train.item()})
        wandb.log({"loss_val": loss_val.item()})
        wandb.log({"acc_train": acc_val.item()})

        print('Epoch: {:04d}'.format(epoch + 1),
              'loss_train: {:.4f}'.format(loss_train.item()),
              'acc_train: {:.4f}'.format(acc_train.item()),
              'loss_val: {:.4f}'.format(loss_val.item()),
              'acc_val: {:.4f}'.format(acc_val.item()),
              'time: {:.4f}s'.format(time.time() - t))

        time_elapsed = time.time() - t_total
        print('Training complete in {:.0f}m {:.0f}s'.format(
            time_elapsed // 60, time_elapsed % 60))
        print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)

    wandb.log({"total_time": (time.time() - t_total)})

    return model, loss_train

# Load data
adj, features, labels, idx_train, idx_val, idx_test = load_data(path)
adj = adj.coalesce().to_dense()


@hydra.main(config_path="configs", config_name="config")
def main(cfg):
    print(torch.__version__)
    # print(OmegaConf.to_yaml(cfg))
    # wandb.config
    wandb.config.update(cfg)

    check_cuda(cfg)


    # Model and optimizer
    model = GCN(nfeat=features.shape[1],
                nhid=cfg.training.hidden,
                nclass=labels.max().item() + 1,
                dropout=cfg.training.dropout)
    optimizer = optim.Adam(model.parameters(),
                           lr=cfg.training.lr, weight_decay=cfg.training.weight_decay)

    imp_cuda(cfg, model, adj, features, labels, idx_train, idx_val, idx_test)

    # Decay LR by a factor of 0.1 every 7 epochs
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

    model_ft, loss = train(cfg, model, optimizer, exp_lr_scheduler, adj, features, labels, idx_train, idx_val)


    #Save model
    PATH = 'checkpoints/model.pt'

    torch.save({
                'epoch': cfg.training.epochs,
                'model_state_dict': model_ft.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': loss,
                }, path+PATH)

    print("Optimization Finished!")
    #print("Total time elapsed: {:.4f}s".format(time.time() - t_total))


    # Testing
    print('Testing the trained GNN model++++++++++++++++++++')
    test(model, adj, features, labels, idx_test)

    root_dir = 'onnix_model'


    print('Exporting ONNIX model using Pytorch++++++++++++++')
    export_onnix(root_dir, model, features, adj, path)


    #ONNIX runtime
    print('Runtime ONNIX model using Pytorch+++++++++++++++++')

    aab = input().split(',')
    predictions = ColaPredictor(path).predict(aab)
    print('Predictions: ', predictions)

    print('Finished adding to WaB+++++++++++++++++++++++++++++')
    run.finish()


if __name__ =="__main__":
    main()
