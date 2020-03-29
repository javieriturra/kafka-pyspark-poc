from pyspark.sql import SparkSession
from pyspark.sql.functions import struct, to_json, expr


class KafkaToConsoleApp:
    """
    The KafkaToConsoleApp reads records from a Kafka topic and show them in the console
    """

    def __init__(self):
        self.spark = SparkSession.builder.master("local[*]").getOrCreate()
        print(self.spark.sparkContext.getConf().getAll())

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        print("Showing batch: %s..." % batch_id)
        micro_batch_df \
            .withColumn("key", expr("string(key)")) \
            .withColumn("value", expr("string(value)")) \
            .show(truncate=False)

    def load(self):
        events_df = self.get_events_df()

        events_df.writeStream \
            .outputMode("append") \
            .trigger(processingTime='5 seconds') \
            .foreachBatch(self.write_micro_batch) \
            .start()

        self.spark.streams.awaitAnyTermination()

    def get_events_df(self):
        events_df = self.spark.readStream.format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("kafka.compression.type", "gzip") \
            .option("subscribe", "events") \
            .load()

        return events_df


if __name__ == '__main__':
    x = KafkaToConsoleApp()
    x.load()
