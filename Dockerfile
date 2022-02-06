FROM python:3.8.12-bullseye
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
RUN flask create_tables
RUN flask import_data


CMD ["deploy.sh"]