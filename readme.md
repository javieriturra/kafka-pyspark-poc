# Kafka PySpark POC

## Prerequisites

- Docker
- Anaconda
- PyCharm

## First Steps

Configure Anaconda Environment:

```conda env create -f pyspark-env.yml```

Verify:

```conda env list```

Open project with PyCharm using the recently created conda environment.  

Download extra jar dependencies, needed for Spark Kafka Integration. 
You can use the provided script:

```./download-dependencies.sh```

## Run the services

Up the docker service kafka, provided into the folder docker-build-kafka, i.e.:

```cd docker-build-kafka```

```docker-compose up```

## Run the apps

To run the apps, use PyCharm's right click menu on the files:
1. RateToKafkaApp.py: to produce events
2. KafkaToConsoleApp.py: to consume events

Alternatively, you can run the apps in the console:

1. ```~/anaconda3/envs/pyspark-env/bin/python RateToKafkaApp.py```
2. ```~/anaconda3/envs/pyspark-env/bin/python KafkaToConsoleApp.py```
