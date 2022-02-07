FROM python:3.8-slim
COPY . /usr/src/app
RUN apt update && apt install -y dnsutils
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
RUN flask create_tables
RUN flask import_data


CMD ["deploy.sh"]