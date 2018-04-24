FROM python:3.6.5-alpine3.7
MAINTAINER xiao_xing <xingxiao@htsc.com>
RUN apk update
RUN apk add wget curl gcc curl-dev musl-dev python3-dev openssl-dev git
ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
RUN git clone https://github.com/xing-xiao/Titans.git
ADD TsapCEPEngine-assembly-0.1.jar /opt/jars/TsapCEPEngine.jar
WORKDIR /Titans/src/restfull/
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOST 9527
CMD ["python3", "run.py"]

