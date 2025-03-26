
docker build -t project .

docker run -it -v ${PWD}/src:/app/src --entrypoint bash project

#to copy data folder from container to your local machine use command:
docker cp my_temp_container:/app/data ./data

#check if everything is working with code: 

''
import transformers
import torch
import pandas as pd
import sklearn

print("Hello World!")

pathway = "./toxic-comment-classification/train.csv/train.csv"

df = pd.read_csv(pathway)

print(df.head())
''

#you are able to run the code in terminal using python train.py