import subprocess
import os

print("Start of batch workflow...")

script_path = os.path.join(os.path.dirname(__file__), "run.py")
subprocess.run(["/usr/local/bin/python", script_path], check=True)

print("Batch workflow complete.")