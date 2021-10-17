
# Ferrato


[![Build Status](https://dev.azure.com/mhew/data-science-template/_apis/build/status/data-science-template?branchName=master)](https://dev.azure.com/mhew/data-science-template/_build/latest?definitionId=15&branchName=master)


---
![Ferrato](https://github.com/Sparten-Ashvinee/Ferrato/blob/master/food.png)
<img src="https://github.com/Sparten-Ashvinee/Ferrato/blob/master/food.png" width="24px">
<img src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Earth.gif" width="24px">


# Requirements
- [yacs](https://github.com/rbgirshick/yacs) (Yet Another Configuration System)
- [PyTorch](https://pytorch.org/) (An open source deep learning platform) 
- [ignite](https://github.com/pytorch/ignite) (High-level library to help with training neural networks in PyTorch)

#### Setup using
```
cd data-science-template
python -m venv dst-env
```

### Data

The modified Boston housing dataset consists of 489 data points, with each datapoint having 3 features. This dataset is a modified version of the Boston Housing dataset found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/).


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



## Training

To train the model(s) in the paper, run this command:

```train
python train.py --input-data <path_to_data> --alpha 10 --beta 20
```

>📋  Describe how to train the models, with example commands on how to train the models in your paper, including the full training procedure and appropriate hyperparameters.

## Evaluation

To evaluate my model on ImageNet, run:

```eval
python eval.py --model-file mymodel.pth --benchmark imagenet
```

>📋  Describe how to evaluate the trained models on benchmarks reported in the paper, give commands that produce the results (section below).

## Pre-trained Models

You can download pretrained models here:

- [My awesome model](https://drive.google.com/mymodel.pth) trained on ImageNet using parameters x,y,z. 

>📋  Give a link to where/how the pretrained models can be downloaded and how they were trained (if applicable).  Alternatively you can have an additional column in your results table with a link to the models.

## Results

Our model achieves the following performance on :

### [Image Classification on ImageNet](https://paperswithcode.com/sota/image-classification-on-imagenet)

| Model name         | Top 1 Accuracy  | Top 5 Accuracy |
| ------------------ |---------------- | -------------- |
| My awesome model   |     85%         |      95%       |

>📋  Include a table of results from your paper, and link back to the leaderboard for clarity and context. If your main result is a figure, include that figure and link to the command or notebook to reproduce it. 





## Generated Project Contents
Depending upon the selected options when creating the project, the generated structure will look similar to the below:

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── data
│   ├── interim_[desc]       <- Interim files - give these folders whatever name makes sense.
│   ├── processed            <- The final, canonical data sets for modeling.
│   ├── raw                  <- The original, immutable data dump.
│   ├── temp                 <- Temporary files.
│   └── training             <- Files relating to the training process
│
├── docs                     <- Documentation
│   ├── data_science_code_of_conduct.md  <- Code of conduct.
│   ├── process_documentation.md         <- Standard template for documenting process and decisions.
│   └── writeup              <- Sphinx project for project writeup including auto generated API.
│      ├── conf.py           <- Sphinx configurtation file.
│      ├── index.rst         <- Start page.
│      ├── make.bat          <- For generating documentation (Windows)
│      └── Makefikle         <- For generating documentation (make)
│
├── examples                 <- Add folders as needed e.g. examples, eda, use case
│
├── extras                   <- Miscellaneous extras.
│   └── add_explorer_context_shortcuts.reg    <- Adds additional Windows Explorer context menus for starting jupyter.
│
├── notebooks                <- Notebooks for analysis and testing
│   ├── eda                  <- Notebooks for EDA
│   │   └── example.ipynb    <- Example python notebook
│   ├── features             <- Notebooks for generating and analysing features (1 per feature)
│   ├── modelling            <- Notebooks for modelling
│   └── preprocessing        <- Notebooks for Preprocessing 
│
├── scripts                  <- Standalone scripts
│   ├── deploy               <- MLOps scripts for deployment (WIP)
│   │   └── score.py         <- Scoring script
│   ├── train                <- MLOps scripts for training
│   │   ├── submit-train.py  <- Script for submitting a training run to Azure ML Service
│   │   ├── submit-train-local.py <- Script for local training using Azure ML
│   │   └── train.py         <- Example training script using the iris dataset
│   ├── example.py           <- Example sctipt
│   └── MLOps.ipynb          <- End to end MLOps example (To be refactored into the above)
│
├── src                      <- Code for use in this project.
│   └── examplepackage       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       ├── features.py      <- Feature engineering functionality
│       ├── io.py            <- IO functionality
│       └── pipeline.py      <- Pipeline functionality
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    ├── examplepackage       <- examplepackage tests
        ├── examplemodule    <- examplemodule tests (1 file per method tested)
        ├── features         <- features tests
        ├── io               <- io tests
        └── pipeline         <- pipeline tests
```


<h2 align="center"><u><b>Workflow</b></u></h2>

<p align="center">
  <img style="width:26rem; height:auto" src="https://raw.githubusercontent.com/Elanza-48/Elanza-48/41a4790484e268102dfdab2b7c59d440d3ffafab/resources/img/coders-prog.gif"/>
</p>

<h3 align="center">Languages</h3>
<p align="center">
  <a href="https://www.cprogramming.com/" target="_blank"> 
    <img src="https://img.shields.io/badge/C%20programming-A8B9CC.svg?style=for-the-badge&logo=c&logoColor=white"
      alt="c"/>
  </a>
  <a href="https://www.java.com" target="_blank"> 
    <img src="https://img.shields.io/badge/Java-007396.svg?style=for-the-badge&logo=java&logoColor=white" 
      alt="java"/> 
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> 
    <img src="https://img.shields.io/badge/Javascript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black"
      alt="javascript"/> 
  </a>
  <a href="https://www.w3.org/html/" target="_blank"> 
    <img src="https://img.shields.io/badge/html-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"
      alt="html5"/> 
  </a>
  <a href="https://www.w3schools.com/css/" target="_blank">
    <img src="https://img.shields.io/badge/css-1572B6.svg?style=for-the-badge&logo=css3&logoColor=white"
      alt="css3"/>
  </a>
  <a href="https://www.typescriptlang.org/" target="_blank"> 
    <img src="https://img.shields.io/badge/typescript-3178C6.svg?style=for-the-badge&logo=typescript&logoColor=white"
      alt="typescript"/>
  </a>
</p>

<h3 align="center">Frontend</h3>
<p align="center">
      <a href="https://getbootstrap.com" target="_blank">
    <img src="https://img.shields.io/badge/bootstrap-7952B3.svg?style=for-the-badge&logo=bootstrap&logoColor=white"
      alt="bootstrap"/>
  </a>
  <a href="https://babeljs.io/" target="_blank">
    <img src="https://img.shields.io/badge/babel-F9DC3E.svg?style=for-the-badge&logo=babel&logoColor=black" alt="babel"/> 
  </a>
  <a href="https://bulma.io/" target="_blank">
    <img src="https://img.shields.io/badge/bulma-00D1B2.svg?style=for-the-badge&logo=bulma&logoColor=white"
      alt="bulma"/>
  </a>
  <a href="https://www.gatsbyjs.com/" target="_blank">
    <img src="https://img.shields.io/badge/gatsbyjs-663399.svg?style=for-the-badge&logo=gatsby&logoColor=white" alt="gatsby" />
  </a>
  <a href="https://reactjs.org/" target="_blank"> 
    <img src="https://img.shields.io/badge/reactjs-61DAFB.svg?style=for-the-badge&logo=react&logoColor=black"
      alt="react"/> 
  </a>
  <a href="https://redux.js.org" target="_blank"> 
    <img src="https://img.shields.io/badge/redux-764ABC.svg?style=for-the-badge&logo=redux&logoColor=white" alt="redux"/> 
  </a> 
  <a href="https://jquery.com/" target="_blank">
    <img src="https://img.shields.io/badge/jquery-0769AD.svg?style=for-the-badge&logo=jquery&logoColor=white" alt="jquery"/> 
  </a>
  <a href="https://webpack.js.org" target="_blank">
    <img src="https://img.shields.io/badge/webpack-8DD6F9.svg?style=for-the-badge&logo=webpack&logoColor=black"
      alt="webpack"/>
  </a>
</p>

<h3 align="center">Backend</h3>
<p align="center">
  <a href="https://nodejs.org" target="_blank"> 
    <img src="https://img.shields.io/badge/node.js-339933.svg?style=for-the-badge&logo=nodedotjs&logoColor=white"
      alt="nodejs"/> 
  </a>
  <a href="https://expressjs.com" target="_blank">
    <img src="https://img.shields.io/badge/express-000000.svg?style=for-the-badge&logo=express&logoColor=white"
      alt="express" />
  <a href="https://hibernate.org/" target="_blank"> 
    <img src="https://img.shields.io/badge/hibernate-59666C.svg?style=for-the-badge&logo=hibernate&logoColor=white" alt="hibernate " /> 
  </a>
    <a href="https://spring.io/" target="_blank"> 
      <img src="https://img.shields.io/badge/spring%20IOC-6DB33F.svg?style=for-the-badge&logo=spring&logoColor=white" alt="spring" /> 
  </a>
  <a href="https://spring.io/" target="_blank"> 
    <img src="https://img.shields.io/badge/spring%20boot-6DB33F.svg?style=for-the-badge&logo=springboot&logoColor=white" alt="spring Boot" /> 
  </a>
  <a href="https://graphql.org" target="_blank">
    <img src="https://img.shields.io/badge/graphql-E10098.svg?style=for-the-badge&logo=graphql&logoColor=white" alt="graphql" />
  </a>
  <a href="https://kubernetes.io" target="_blank"> 
    <img src="https://img.shields.io/badge/kubernetes-326CE5.svg?style=for-the-badge&logo=kubernetes&logoColor=white" alt="kubernetes"/>
  </a>
  <a href="https://www.nginx.com" target="_blank"> 
    <img src="https://img.shields.io/badge/nginx-009639.svg?style=for-the-badge&logo=nginx&logoColor=white" alt="nginx"/> 
  </a>
</p>

<h3 align="center">Database</h3>
<p align="center">
  <a href="https://www.postgresql.org" target="_blank"> 
    <img src="https://img.shields.io/badge/postgreSQL-4169E1.svg?style=for-the-badge&logo=postgresql&logoColor=white"
      alt="postgresql"/> 
  </a>
  <a href="https://redis.io" target="_blank"> 
    <img src="https://img.shields.io/badge/redis-DC382D.svg?style=for-the-badge&logo=redis&logoColor=white"
      alt="redis"/>
  </a>
  <a href="https://www.sqlite.org/" target="_blank"> 
    <img src="https://img.shields.io/badge/sqlite-003B57.svg?style=for-the-badge&logo=sqlite&logoColor=white"
      alt="sqlite"/> 
  </a>
  <a href="https://www.mongodb.com/" target="_blank"> 
    <img src="https://img.shields.io/badge/mongodb-47A248.svg?style=for-the-badge&logo=mongodb&logoColor=white"
      alt="mongodb"/> 
  </a> 
</p>

<h3 align="center">Cloud & Hosting:</h3>
<p align="center">
  <a href="https://azure.microsoft.com/en-in/" target="_blank">
    <img  src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="azure"/> 
  </a>
  <a href="https://firebase.google.com/" target="_blank">
    <img src="https://img.shields.io/badge/firebase-FFCA28.svg?style=for-the-badge&logo=firebase&logoColor=black" alt="firebase"/>
  </a>
  <a href="https://netlify.com/" target="_blank">
    <img src="https://img.shields.io/badge/netlify-00C7B7.svg?style=for-the-badge&logo=netlify&logoColor=black" alt="firebase"/>
  </a>
  <a href="https://heroku.com" target="_blank"> 
    <img src="https://img.shields.io/badge/heroku-430098.svg?style=for-the-badge&logo=heroku&logoColor=white"
      alt="heroku"/> 
  </a> 
</p>

<h3 align="center">Testing</h3>
<p align="center"> 
  <a href="https://www.selenium.dev" target="_blank"> 
    <img src="https://img.shields.io/badge/selenium-43B02A.svg?style=for-the-badge&logo=selenium&logoColor=white"
      alt="selenium" /> 
  </a> 
  <a href="https://junit.org/junit5/" target="_blank"> 
    <img src="https://img.shields.io/badge/junit-25A162.svg?style=for-the-badge&logo=junit5&logoColor=white" alt="junit5" /> 
  </a> 
</p>

<h3 align="center">Version Control & CI/CD</h3>
<p align="center">
  <a href="https://git-scm.com/" target="_blank">
    <img src="https://img.shields.io/badge/git-F05032.svg?style=for-the-badge&logo=git&logoColor=white"
      alt="git"/>
  </a>
  <a href="https://github.com/ELanza-48" target="_blank">
    <img src="https://img.shields.io/badge/github-181717.svg?style=for-the-badge&logo=github&logoColor=white" alt="github" />
  </a>
  <a href="https://gitlab.com/Elanza-48" target="_blank">
    <img src="https://img.shields.io/badge/gitlab-181717.svg?style=for-the-badge&logo=gitlab&logoColor=white"
      alt="git"/>
  </a>
    <a href="https://www.docker.com/" target="_blank">
    <img src="https://img.shields.io/badge/docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white"
      alt="docker"/>
  </a>
  <a href="https://www.jenkins.io" target="_blank"> 
    <img src="https://img.shields.io/badge/jenkins-D24939.svg?style=for-the-badge&logo=jenkins&logoColor=white" alt="jenkins"/> 
  </a>
</p>

<h3 align="center">Preferred IDEs  & Tools :</h3>
<p align="center"> 
  <a href="https://eclipse.org" target="_blank">
    <img src="https://img.shields.io/badge/eclipse-2C2255.svg?style=for-the-badge&logo=eclipse&logoColor=white" alt="eclipse IDE"/> 
  </a>
  <a href="https://code.visualstudio.com/" target="_blank">
    <img src="https://img.shields.io/badge/vscode-007ACC.svg?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="vsCode"/> 
  </a>
  <a href="https://www.jetbrains.com/" target="_blank">
    <img src="https://img.shields.io/badge/jetbrains%20IDE-000000.svg?style=for-the-badge&logo=jetbrains&logoColor=white" alt="jetbrains" />
  </a>
  <a href="https://postman.com" target="_blank"> 
    <img src="https://img.shields.io/badge/postman-FF6C37.svg?style=for-the-badge&logo=postman&logoColor=white" alt="postman"/>
  </a>
  <a href="https://www.virtualbox.org/" target="_blank">
    <img src="https://img.shields.io/badge/virtualbox-183A61.svg?style=for-the-badge&logo=virtualbox&logoColor=white"
      alt="virtualbox"/>
  </a>
  <a href="https://ubuntu.com/" target="_blank"> 
    <img src="https://img.shields.io/badge/ubuntu-E95420.svg?style=for-the-badge&logo=ubuntu&logoColor=white" alt="ubuntu"/>
  </a>
</p>

----



-------------------------------------------------------------------------------------------------------------------------------------------------------


<h2 align="center">
My Current Workstation Specification </h2>

<div align="center">
	

![CPU](https://img.shields.io/badge/AMD-Ryzen_5_3500X-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
<br> 
	
![GPU](https://img.shields.io/badge/AMD-Radeon_RX_550-ED1C24?style=for-the-badge&logo=amd&logoColor=white) 



</div>

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
