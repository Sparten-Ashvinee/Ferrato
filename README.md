
# Ferrato


---
![Ferrato](https://github.com/Sparten-Ashvinee/Ferrato/blob/master/food.png)

# Requirements
[All the common python packages along with versions are present in the requirements.txt file]
- torch == 1.9.1
- torch-geometric == 2.0.1
- torchvision == 0.10.1
- tensorboard==2.5.0
- boto3==1.17.106
- dvc==2.8.1
- fastapi==0.70.0
- Hydra==2.5
- networkx==2.6.3
- onnxruntime==1.9.0
- mlflow==1.20.2
- wandb==0.12.4


### Dataset
Initiated working on the dataset collection process from scratch on Indian recipes and their corresponding ingredients. Indian recipes along with its ingredients are extracted from more than 25 different webpages. You can check the graphical representation that illustrates the recipes interconnection based on shared ingredients in the notebook section. For instance, the recipe for Lemon Air Fryer Broccolini require ingredients such as Fresh broccolini, Lemon, and Olive oil. 

### Model
Our approach centered around implementing a Graph Neural Network (GNN) for analyzing the Indian recipe dataset. A GNN is neural network designed to handle complex relationships and interactions between entities represented as nodes and edges in a graph. We can say, A GNN is an optimizable transformation on all attributes of the graph (nodes, edges, global context) that preserves graph symmetries (permutation invariances).  
For your project, GNNs can be particularly useful for analyzing the Indian recipe dataset since they can model the relationships between recipes based on shared ingredients. By representing recipes as nodes and shared ingredients as edges, a GNN can learn to recommend similar recipes, suggest alternative ingredients, or discover new recipe combinations based on the learned embeddings.

### MLOps steps


<img src="https://github.com/Sparten-Ashvinee/Ferrato/blob/5fc6f1d3c57617bf7ad316555a8911cb9c5cbc1c/imgs/workflows2.png">
## Training

To train the model(s) in the paper, run this command:

```train
python train.py --input-data <path_to_data> --alpha 10 --beta 20
```


-----------------------------------------------------------------------------------------------------------------------------------------------------------------







## References
* https://github.com/Statoil/data-science-template/ - The master template for this project
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP
* https://drivendata.github.io/cookiecutter-data-science/
* https://github.com/audreyr/cookiecutter-pypackage

<h3 align="center">Connect with me</h3>

<div style="margin-top:10px" align="center">
  <div>
    <a  href="https://linkedin.com/in/example" target="_blank">
      <img src="https://img.shields.io/badge/Linked%20In-0A66C2.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="example"/>
    </a>
    <a href="https://twitter.com/example" target="_blank">
      <img src="https://img.shields.io/badge/Twitter-1DA1F2.svg?style=for-the-badge&logo=twitter&logoColor=white" alt="example"/>
    </a>
  </div>
</div> 
