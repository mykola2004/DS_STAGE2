import os
import subprocess

CONFIG_DIR = "./configs"

for filename in sorted(os.listdir(CONFIG_DIR)):
    if filename.endswith(".json"):
        path = os.path.join(CONFIG_DIR, filename)
        subprocess.run(["python", "src/train.py", path])