FROM python:3
MAINTAINER david.michael.tucker@gmail.com

RUN pip install --upgrade pip
RUN pip install pep8 pylint

WORKDIR /src
COPY . .
RUN pep8 backlog
RUN pylint backlog
RUN python -m unittest discover
RUN pep8 setup.py
RUN pylint setup.py
RUN rm -rf dist
RUN python setup.py sdist
RUN pip install dist/*
WORKDIR /

ENTRYPOINT ["backlog"]
