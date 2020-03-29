#!/usr/bin/env bash

rm -rf /tmp/*
KAFKA_HOME=${KAFKA_HOME}
"${KAFKA_HOME}"/bin/zookeeper-server-start.sh "${KAFKA_HOME}"/config/zookeeper.properties > /dev/null 2>&1 &
"${KAFKA_HOME}"/bin/kafka-server-start.sh "${KAFKA_HOME}"/config/server.properties
