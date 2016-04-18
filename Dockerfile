FROM python:2
MAINTAINER david.michael.tucker@gmail.com

RUN pip install --upgrade pip

WORKDIR /src
COPY . .
RUN rm -rf dist
RUN python setup.py sdist
RUN pip install dist/*
WORKDIR /

ENTRYPOINT ["backlog"]
