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
    def __init__(self, path,model_path, batch_size, max_length, features, adj):
        # creating the onnxruntime session
        self.path = path
        model_path = self.path+"onnix_model/models/model.onnx"
        self.ort_session = ort.InferenceSession(model_path)
        #self.processor = DataModule()
        self.lables = ["class1", "class2"]
        #model_name = "google/bert_uncased_L-2_H-128_A-2"
        self.batch_size = batch_size
        self.max_length = max_length
        #model = TFDistilBertForSequenceClassification.from_pretrained(model_name, num_labels=7)
        #self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.features = features
        self.adj = adj

    def sigmoid(self, x):
        return 1/(1+math.exp(-x))

    # def tokenize_data(self, example):
    #     return self.tokenizer(
    #         example["sentence"],
    #         truncation=True,
    #         padding="max_length",
    #         max_length=self.max_length,
    #     )

    def to_numpy(self, tensor):
         return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

    def predict(self, PATH, model, aab=['salt', 'egg', 'oil', 'rice', 'chile', 'onion']):
        #salt, egg, oil, rice, chile, onion
        #inference_sample = {"sentence": text}
        #processed = self.tokenize_data(inference_sample)

        # # Preparing inputs
        # ort_inputs = {
        #     "features": np.expand_dims(processed["input_ids"], axis=0),
        #     "adj": np.expand_dims(processed["attention_mask"], axis=0),
        # }
        #
        # Run the model (None = get all the outputs)
        #ort_inputs2 = {self.ort_session.get_inputs()[0].name: self.to_numpy(processsed)}
        #
        # ort_inputs = {
        #     "features": torch.from_numpy(np.array(ort_inputs['features'], dtype=np.float32)).cpu().numpy(),
        #     "adj": torch.from_numpy(np.array(ort_inputs['adj'], dtype=np.float32)).cpu().numpy(),
        # }

        #model.load_state_dict(torch.load(PATH))
        checkpoint = torch.load(PATH)
        model.load_state_dict(checkpoint['model_state_dict'])
        all_ingss = list(pd.read_csv(self.path+'Data/all_ingredients_name.csv')['In'])
        ing_len = len(all_ingss)
        new_arr = np.zeros(ing_len).astype(int)

        for item in aab:
            ing_str = item.replace(" ", "")
            indx = all_ingss.index(ing_str)
            new_arr[indx] = 1

        new_arr = np.array([0] + list(new_arr)).astype(int)
        feat = self.features[:853, :]
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
            "adj": np.expand_dims(self.adj,  axis=0),
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
        output = model(feats, self.adj)
        output = [round(i) for i in output[0].tolist()]

        if output[0] < output[1]:
            predictions = 'Non-Indian'
        elif output[0] > output[1]:
            predictions = 'Indian'
        else:
            predictions = 'Please provide more INFORMATION!'

        return predictions


