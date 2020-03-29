FROM openjdk:8-slim

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y unzip

WORKDIR /opt

ARG KAFKA_VERSION="0.10.2.2"
ARG SCALA_VERSION="2.11"
ARG KAFKA_BIN="kafka_${SCALA_VERSION}-${KAFKA_VERSION}"
ARG KAFKA_DOWNLOAD="http://archive.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_BIN}.tgz"

RUN wget ${KAFKA_DOWNLOAD}
RUN tar -zxvf ${KAFKA_BIN}.tgz

RUN ln -s ${KAFKA_BIN} kafka

ARG KAFKA_HOME=/opt/kafka
ENV KAFKA_HOME=${KAFKA_HOME}

RUN rm /opt/*tgz

COPY entrypoint.sh /opt
COPY server.properties /opt/kakfa/config/
