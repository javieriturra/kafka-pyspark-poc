from RateToConsoleApp import RateToConsoleApp
from pyspark.sql.functions import expr


class RateToKafkaApp(RateToConsoleApp):
    """
    The RateToConsoleApp reads records from a Rate stream and write them to a Kafka Topic
    """

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        print("Writing batch: %s to kafka..." % batch_id)
        micro_batch_df \
            .withColumn("topic", expr("'events'")).write \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .save()


if __name__ == '__main__':
    x = RateToKafkaApp()
    x.load()
