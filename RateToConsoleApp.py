from pyspark.sql import SparkSession
from pyspark.sql.functions import struct, to_json, expr
import time


class RateToConsoleApp:
    """
    The RateToConsoleApp reads records from a Apache Spark rate (fake) stream and shows them in the console.
    Useful to emulate events.
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
        events_df = self.get_events_df()

        events_df.writeStream \
            .outputMode(output_mode) \
            .trigger(processingTime=self.processingTime) \
            .foreachBatch(self.write_micro_batch) \
            .start()

        self.spark.streams.awaitAnyTermination()

    def get_events_df(self):
        rate_df = self.spark.readStream.format("rate").load()
        events_df = rate_df \
            .withColumn("key", expr("uuid()")) \
            .withColumn("value",
                        to_json(struct(rate_df["value"].alias("ordinal"),
                                       expr("value % 3 +1").alias("locationId"),
                                       rate_df["timestamp"],
                                       expr("floor(rand() * 100000000 / 100)").alias("amount")))) \
            .select("key", "value")

        return events_df


if __name__ == '__main__':
    x = RateToConsoleApp('5 seconds')
    x.load("append")
