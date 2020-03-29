from pyspark.sql import SparkSession
from pyspark.sql.functions import struct, to_json, expr


class RateToConsoleApp:
    """
    The RateToConsoleApp reads records from a Rate stream and show them in the console
    """

    def __init__(self):
        self.spark = SparkSession.builder.master("local[*]").getOrCreate()
        print(self.spark.sparkContext.getConf().getAll())

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        print("Showing batch: %s..." % batch_id)
        micro_batch_df.show(truncate=False)

    def load(self):
        events_df = self.get_events_df()

        events_df.writeStream \
            .outputMode("append") \
            .trigger(processingTime='5 seconds') \
            .foreachBatch(self.write_micro_batch) \
            .start()

        self.spark.streams.awaitAnyTermination()

    def get_events_df(self):
        rate_df = self.spark.readStream.format("rate").load()
        events_df = rate_df \
            .withColumn("key", expr("uuid()")) \
            .withColumn("value", to_json(struct(rate_df["value"], rate_df["timestamp"]))) \
            .select("key", "value")
        return events_df


if __name__ == '__main__':
    x = RateToConsoleApp()
    x.load()
