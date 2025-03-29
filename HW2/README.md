## Introduction
Let's assume, that the project you are working on is about natural language processing and framework you want to use is transformers. There is no need to download dataset(which is accessible with this link: https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data) and all necessary frameworks on your own. All you need is to just follow all instructions one by one presented in this README. At the end, you will get set up environment with all configurations, installed libraries and prepared dataset for you to work.  

## Prerequisites
Firstly, you will need to have installed on your local machine docker, git and some IDE. After that please clone the repository on you local machine.
Having these things, you can go on to next section.

## Main instructions
1. Open bash on your laptop, navigate to cloned project and use this command to build an image out of docker file:
```bash
docker build -t project .
```

2. After the image is built, please use this command to run a container:
```bash
docker run -it -v ${PWD}/src:/app/src --entrypoint bash project
```

## Project description
Now, the project is fully set up in a container. 

Structure of project on your local machine:
```
app
├── data_loader          # Script that automatically loads data (runs automatically while building an image)
│   └── data_load.py        
├── src                  # Here will be stored future script files of project
│   └── main.py
├── .dockerignore        # List of files ignored by docker
├── .gitignore           # List of files ignored by git
├── requirements.txt     # File listing all necessary libraries used for training
├── dockerfile           
└── README.md            # Descriprion of the project, instruction how to launch a project
```

The structure of project in container: 
```
HW2
├── data                 # Folder with data sets
│   ├── test.csv
│   ├── test_labels.csv
│   └── train.csv
├── data_loader          # Script that automatically loads data (runs automatically while building an image)
│   └── data_load.py        
├── src                  # Here will be stored future script files of project
│   └── main.py
└── requirements.txt     # File listing all necessary libraries used for training
```

Now, you are able to change files in folder /src locally, which will be visible in container. For example, you can create new file1.py file and paste in it following code:
```python
import transformers as transf
import torch as trch
import pandas as pd
import sklearn as skl

print("Hello World!")

pathway = "../data/train.csv"
df = pd.read_csv(pathway)

print(df.head())

print("It works!")
```

Then, save the file locally, go on to bash of running container, navigate to folder /app/src inside container and run the script with the command:
```bash
python file1.py
```

## NOTE
If you want to copy data folder from container to your local machine use command(open bash on your laptop, navigate to cloned project):
```bash
docker cp ID_CONTAINER:/app/data ./data
```

, where ID_CONTAINER - is the real id of container you got earlier