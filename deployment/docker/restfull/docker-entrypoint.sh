#!/bin/sh
FLINK_SERVER=http://jobmanager:8081/
JAR_PATH=/opt/jars/

sleep 30

curl -XPOST ${FLINK_SERVER}jars/upload -H "Expect:" -F "jarfile=@${JAR_PATH}TsapCEPEngine.jar" > ${JAR_PATH}tasks.name

