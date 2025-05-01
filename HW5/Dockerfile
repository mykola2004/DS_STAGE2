FROM python:3.10-slim

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY batch_deployment/cronjob.sh /etc/cron.d/batchjob

RUN chmod 0644 /etc/cron.d/batchjob
RUN crontab /etc/cron.d/batchjob

EXPOSE 5000

CMD ["sh", "-c", "cron && python rest_api/app.py"]