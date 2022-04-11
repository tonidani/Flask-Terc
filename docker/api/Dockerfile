FROM python:3.8-slim
RUN apt update && apt install -y dnsutils netcat postgresql-client
RUN mkdir -p /usr/src/app/
COPY requirements.txt /usr/src/app/
RUN pip install python-dotenv
RUN pip install -r /usr/src/app/requirements.txt
WORKDIR /usr/src/app
COPY docker/api/deploy.sh /usr/bin/wait4db
RUN chmod +x /usr/bin/wait4db
ADD . /usr/src/app
