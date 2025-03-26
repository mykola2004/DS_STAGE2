import os
import gdown
print("Hello")

os.makedirs("/data", exist_ok=True)

url = f"https://drive.google.com/drive/folders/1X_qEe5ihHrdF_sWsnSuLw22s4Su7ZLMg?hl=PL"

gdown.download_folder(url=url, output="/data", quiet=False, use_cookies=False)

print("Data downloaded to /data")