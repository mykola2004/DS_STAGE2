import os
import gdown

os.makedirs("/data", exist_ok=True)

folder_id = "1X_qEe5ihHrdF_sWsnSuLw22s4Su7ZLMg?usp=sharing"
url = f"https://drive.google.com/drive/folders/{folder_id}"

gdown.download_folder(url=url, output="/data", quiet=False, use_cookies=False)