import copyreg
import math
import pickle
import pandas as pd
import torch
from onnxruntime import  get_all_providers
import onnxruntime as ort
import numpy as np
import scipy.sparse as sp
#from transformers import AutoTokenizer
#from transformers import TFDistilBertForSequenceClassification
from utils import load_data
from models import GCN



def export_onnix(root_dir, model, features, adj, path):

    #Trained model which needs to be converted
    #model_path = "/home/ashvinee/Documents/Ferrato/checkpoints"
    #cola_model = ColaModel.load_from_checkpoint(model_path)

    feat = torch.zeros(features.shape[0], features.shape[1])
    adje = torch.zeros(adj.shape[0], adj.shape[1])

    torch.onnx.export(
        model,  # model being run
        ( feat, adje),  # model input (or a tuple for multiple inputs)
        path + "onnix_model/models/model.onnx",  # where to save the model
        export_params=True,
        opset_version=10,
        input_names=["features", "adj"],  # the model's input names
        output_names=["output"],  # the model's output names
        dynamic_axes={  # variable length axes
            "features": {0: "batch_size"},
            "adj": {0: "batch_size"},
            "output": {0: "batch_size"},
        },
    )



class ColaPredictor:
    def __init__(self, path):
        # creating the onnxruntime session
        self.path = path
        model_path = self.path+"onnix_model/models/model.onnx"
        self.ckpt_path = path+'checkpoints/model.pt'
        self.ort_session = ort.InferenceSession(model_path)
        self.lables = ["class1", "class2"]


    def sigmoid(self, x):
        return 1/(1+math.exp(-x))


    def to_numpy(self, tensor):
         return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

    def predict(self, text=['salt', 'egg', 'oil', 'rice', 'chile', 'onion']):
        #salt, egg, oil, rice, chile, onion


        #model.load_state_dict(torch.load(PATH))
        path = '/home/ashvinee/Documents/Ferrato/'
        adj, features, labels, idx_train, idx_val, idx_test = load_data(path)
        adj = adj.coalesce().to_dense()

        model = GCN(nfeat=features.shape[1],
                    nhid=16,
                    nclass=labels.max().item() + 1,
                    dropout=0.5)

        checkpoint = torch.load(self.ckpt_path)
        model.load_state_dict(checkpoint['model_state_dict'])
        all_ingss = list(pd.read_csv(self.path+'Data/all_ingredients_name.csv')['In'])
        ing_len = len(all_ingss)
        new_arr = np.zeros(ing_len).astype(int)

        for item in text:
            ing_str = item.replace(" ", "")
            indx = all_ingss.index(ing_str)
            new_arr[indx] = 1

        new_arr = np.array([0] + list(new_arr)).astype(int)
        feat = features[:853, :]
        feat = feat.cpu().detach().numpy()

        liss = []
        for i in feat:
            liss.append([int(j) for j in list(i)])

        featt = np.array([list(new_arr)] + liss)
        new_featt = torch.from_numpy(featt)

        TFeat = sp.csr_matrix(new_featt, dtype=np.float32)
        feats = torch.FloatTensor(np.array(TFeat.todense()))

        #Preparing inputs
        ort_inputs = {
            "features": np.expand_dims(feats, axis=0),
            "adj": np.expand_dims(adj,  axis=0),
        }

        '''
        ort_outs = self.ort_session.run(None, ort_inputs)
        
        # Normalising the outputs
        scores = torch.nn.Softmax(ort_outs[0].shape)

        predictions = []
        for score, label in zip(scores, self.lables):
            predictions.append({"label": label, "score": score})
        '''

        model.eval()
        output = model(feats, adj)
        output = [round(i) for i in output[0].tolist()]

        if output[0] < output[1]:
            predictions = 'Non-Indian'
        elif output[0] > output[1]:
            predictions = 'Indian'
        else:
            predictions = 'Please provide more INFORMATION!'

        return predictions


