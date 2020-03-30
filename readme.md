# Kafka PySpark POC

## Prerequisites

- Docker
- Anaconda
- PyCharm (optional)

## First Steps

Configure Anaconda environment, using the provided template

```conda env create -f pyspark-env.yml```

Verify:

```conda env list```

Open project with PyCharm using the recently created conda environment.  

Download extra jar dependencies, needed for Spark Kafka Integration. You can use the provided script:

```./download-dependencies.sh```

## Run the services

Up the docker service kafka, provided into the folder docker-build-kafka, i.e.:

```cd docker-build-kafka```

```docker-compose up```

## Run the apps

To run the apps, use PyCharm's right click menu on the files. Alternatively, you can run the apps in the console.

|Producers           |Consumers                        |
|---                 |---                              |
|RateToConsoleApp.py |KafkaEventCountApp.py            |
|RateToKafkaApp.py   |KafkaEventCountByLocationApp.py  |
|                    |KafkaToConsoleApp.py             |

Please read the documentation to understand what does each program.
