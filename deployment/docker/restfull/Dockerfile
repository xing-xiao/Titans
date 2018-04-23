FROM python:3.6.5-alpine3.7
MAINTAINER xiao_xing <xingxiao@htsc.com>
RUN apk update
RUN apk add wget curl gcc curl-dev musl-dev python3-dev openssl-dev
ADD requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt
WORKDIR /opt/rules-manager
CMD ["python3", "run.py"]