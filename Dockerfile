FROM python:2
MAINTAINER david.michael.tucker@gmail.com

RUN pip install --upgrade pip

COPY . /tmp
RUN cd /tmp && python setup.py build
RUN cd /tmp && pip install .
ENTRYPOINT ["backlog"]
