FROM python:2
MAINTAINER david.michael.tucker@gmail.com

RUN pip install --upgrade pip

COPY . /tmp/backlog
RUN cd /tmp/backlog && python setup.py sdist
RUN cd /tmp/backlog && pip install dist/backlog-*.tar.gz
ENTRYPOINT ["backlog"]
