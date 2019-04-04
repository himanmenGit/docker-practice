FROM python:3.6.7

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/ec2-docker-compose
ADD requirements.txt /srv/ec2-docker-compose

WORKDIR /srv/ec2-docker-compose

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /srv/ec2-docker-compose
