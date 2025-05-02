FROM python:3.10-slim

RUN apt-get update && apt-get install -y cron

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt && pip install -e .

COPY batch_deployment/cronjob.sh /etc/cron.d/batchjob
RUN apt-get update && apt-get install -y dos2unix && dos2unix /etc/cron.d/batchjob
RUN chmod 0644 /etc/cron.d/batchjob
RUN touch /var/log/cron.log && chmod 666 /var/log/cron.log

EXPOSE 5000
CMD ["sh", "-c", "cron && python rest_api/app.py"]