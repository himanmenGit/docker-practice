FROM            python:3.6.7-slim
MAINTAINER      study.himanmen@gmail.com

ENV             LANG C.UTF-8

# apt-get으로 nginx, supervisor 설치
RUN             apt-get -y update
RUN             apt-get -y dist-upgrade
RUN             apt-get -y install build-essential nginx supervisor

# requirements만 복사
COPY            requirements.txt /srv/requirements.txt

# pip install
WORKDIR         /srv
RUN             pip install --upgrade pip
RUN             pip install -r  /srv/requirements.txt
RUN             rm -f           /srv/requirements.txt


ENV             DJANGO_SETTINGS_MODULE config.settings

# 소스 폴더 복사
COPY            . /srv/eb-docker

# nginx 설정 파일 복사 후 링크
RUN             cp -f   /srv/eb-docker/.config/nginx-app.conf         /etc/nginx/sites-available/
RUN             rm -f   /etc/nginx/sites-enabled/*
RUN             ln -sf  /etc/nginx/sites-available/nginx-app.conf   /etc/nginx/sites-enabled/

# supervisor 설정 파일 복사
RUN             cp -f /srv/eb-docker/.config/super_uwsgi.conf         /etc/supervisor/conf.d/

# pkill nginx후 supervisord -n 실행
CMD             nginx; supervisord -n
EXPOSE          80