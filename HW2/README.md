1. 
docker build -t project .
2. 
docker run -it -v ${PWD}:/app project

3. connect with vs code: ctrl+shft+P , then choose 
4. install extnesions pyhton, Dev Containers and Docker by Microsoft
5. check if everything is working with code: 

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

6. you are able to run the code in terminal using python train.py