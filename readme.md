# Kafka PySpark POC

Writen in Python 3, this project introduces basic Structured Streaming features of Apache Spark like:
1. Kafka events producing
1. Kafka events consuming
1. Event Watermarking
1. Unordered data
1. Delayed data 
1. JSON transformations
1. Joins between streaming dataframes and batch dataframes
1. Real Time data aggregation
1. Processing Triggers
1. Real Time processing in micro batch mode
1. Loading batch data

## Prerequisites

- Docker Engine
- Docker Compose
- Anaconda (Python 3)
- PyCharm (optional)

## First Steps

1. Configure Anaconda environment, using the provided template:

```conda env create -f pyspark-env.yml```

2. Verify:

```conda env list```

3. Download extra jar dependencies, needed for Spark Kafka Integration. You can use the provided script:

```./download-dependencies.sh```

Now you can open the project with PyCharm using the recently created conda environment.  

## Run the services

Up the docker service kafka, defined into the folder docker-build-kafka, i.e.:

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
