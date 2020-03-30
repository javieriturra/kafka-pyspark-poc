from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, expr
from pyspark.sql.types import StructType, StructField, TimestampType, LongType
import time


class KafkaToConsoleApp:
    """
    The KafkaToConsoleApp reads records from a Kafka topic and shows them on the console.
    """

    def __init__(self, processing_time):
        self.spark = SparkSession.builder.getOrCreate()
        print("Spark version is: %s" % self.spark.version)
        print(self.spark.sparkContext.getConf().getAll())
        self.processingTime = processing_time

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        ts = time.localtime()
        print("Showing batch %s at %s" % (batch_id, time.strftime("%Y-%m-%d %H:%M:%S", ts)))
        micro_batch_df.show(truncate=False)

    def load(self, output_mode):
        self.get_events_df().writeStream \
            .outputMode(output_mode) \
            .trigger(processingTime=self.processingTime) \
            .foreachBatch(self.write_micro_batch) \
            .start()
        self.spark.streams.awaitAnyTermination()

    def get_events_df(self):
        schema = StructType([StructField("value", LongType(), True), StructField("timestamp", TimestampType(), True)])

        # The events are watermarked on the eventTimestamp custom field (not the kafka timestamp)
        # Delay threshold indicates how much time the system will wait for events based on the watermark
        return self.spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("subscribe", "events") \
            .load() \
            .withColumn("key", expr("string(key)")) \
            .withColumn("value", from_json(expr("string(value)"), schema)) \
            .withColumn("eventValue", expr("value.value")) \
            .withColumn("eventTimestamp", expr("value.timestamp")) \
            .withWatermark(eventTime="eventTimestamp", delayThreshold="30 seconds") \
            .drop("value")


if __name__ == '__main__':
    x = KafkaToConsoleApp(processing_time="10 seconds")
    x.load("append")
