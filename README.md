
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

### Continuous Integration
Continuous Integration (CI) increase quality by building, running tests and performing other validation whenever 
code is committed. The template contains a build pipeline for Azure DevOps, however requires a couple of manual
steps to setup:

* Log in to http://dev.azure.com and browse to, or create an organisation & project. The project name should be the same as your github repository name.
* Under *Pipelines -> Builds select* *New Pipeline*
* Select github and then your repository. Login / grant any permissions as prompted
* In the review pane click *run*

You are now setup for CI and automated test / building. You should verify the badge link in this README corresponds 
with your DevOps project, and as a further step might setup any release pipelines for automated deployment.

At this stage the build pipeline doesn't include MLOps steps, although these can be added based uon your needs.


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
