import os
import gdown

def download_file(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

def main():
    os.makedirs("data", exist_ok=True)

    files = {"datasetp1.csv": "1SR0RLM4zzlHaELc39f9865nr_ko0SZsf",
        "datasetp2.csv": "1eC-4q8xlN4jXiatHgcdSUdLLh1YEb7jj"}

    for filename, file_id in files.items():
        output_path = os.path.join("data", filename)
        download_file(file_id, output_path)
        print("Data saved in folder /data")

if __name__ == "__main__":
    main()