FROM python:3.6
RUN apt update
RUN apt install -y build-essential libpq-dev
RUN apt install -y python3-dev default-libmysqlclient-dev
RUN apt install -y python-boto

LABEL maintainer ="gmjun2000@gmail.com"
ENV ENVIROMENT development
WORKDIR /data/britecore/

# Install reqs
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
