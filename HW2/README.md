## Introduction
Let's assume, that the project you are working on is about natural language processing and framework you want to use is transformers. There is no need to download dataset(which is accessible with this link: https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data) and all necessary frameworks on your own. All you need is to just follow all instructions one by one presented in this README. At the end, you will get set up environment with all configurations, installed libraries and prepared dataset for you to work.  

## Prerequisites
Firstly, you will need to have installed on your local machine docker, git and some IDE. After that please fork the repository on you local machine.
Having these things, you can go on to next section.

## Main instructions
1. Open bash on your laptop and use this command to build an image out of docker file:

```bash
docker build -t project .
```

2. After the image is built, please use this command to run a container:

```bash
docker run -it -v ${PWD}/src:/app/src --entrypoint bash project
```

## Project description
Now, the project is fully set up in a container.


#you are able to run the code in terminal using python train.py

#check if everything is working with code: 

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

## NOTE
If you want to copy data folder from container to your local machine use command:
docker cp ID_CONTAINER:/app/data ./data
where ID_CONTAINER - is the real id of container you got earlier
