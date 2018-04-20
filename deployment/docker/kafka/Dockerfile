FROM java:8
MAINTAINER xiao_xing <xingxiao@htsc.com>
RUN apt-get update
RUN apt-get install -y wget supervisor
RUN wget http://mirrors.hust.edu.cn/apache/kafka/1.0.0/kafka_2.11-1.0.0.tgz && tar -xzf kafka_2.11-1.0.0.tgz && rm -f kafka_2.11-1.0.0.tgz
ADD supervisord.conf /etc/supervisor/supervisord.conf
WORKDIR /kafka_2.11-1.0.0
EXPOSE 9092
CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/supervisord.conf"]
