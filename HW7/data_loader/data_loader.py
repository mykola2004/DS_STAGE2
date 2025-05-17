import gdown
import sys

url = f"https://drive.google.com/uc?id=1USmrmIyTwBm21OdnUkUYOZhywsIhG31f"

gdown.download(url, "./data/dataset.csv", quiet=False)
