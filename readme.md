# Kafka PySpark POC

Written in Python 3, this project introduces basic Structured Streaming features of Apache Spark like:
- Kafka events producing and consuming
- Event Watermarking, Unordered data, Delayed data 
- JSON transformations
- Joins between streaming dataframes and batch dataframes
- Data aggregation in time windows
- Processing Triggers
- Real Time micro batches and output modes (_append_, _update_, _complete_)
- Loading batch data from files. Data caching

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

## Running the Services

Up the docker service kafka, defined into the folder docker-build-kafka, i.e.:

```cd docker-build-kafka```

```docker-compose up```

## Running the Apps

To run the apps, use PyCharm's right click menu on the files. Alternatively, you can run the apps in the console.
The recommendation is to run the apps in __black__ simultaneously.

|Producers            |Consumers                          |
|---                  |---                                |
|RateToConsoleApp.py  |KafkaEventCountApp.py              |
|__RateToKafkaApp.py__|__KafkaEventCountByLocationApp.py__|
|                     |KafkaToConsoleApp.py               | 

Please read the documentation to understand what does each program.

## TODO

- More detail on explanations
- Writing to a Time Series Database
- Spark Cluster Usage
- Real Time Visualization
- More realistic emulated data
- Connecting to a real data source
