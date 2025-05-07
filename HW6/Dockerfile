FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY inference_server.py .
COPY model ./model

EXPOSE 8080

CMD ["python", "inference_server.py"]