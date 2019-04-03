FROM        python:3.6.7
MAINTAINER  study.himanmen@gmail.com
ENV         PYTHONUNBUFFERED 1
RUN         mkdir /web
WORKDIR     /web
COPY        . /web
RUN         pip install --upgrade pip
RUN         pip install -r requirements.txt
