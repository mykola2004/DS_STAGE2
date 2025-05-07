FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev \
    openblas-dev \
    lapack-dev \
    gfortran \
    linux-headers \
    && pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY model ./model

EXPOSE 8080

ENTRYPOINT ["python", "server.py"]
CMD []