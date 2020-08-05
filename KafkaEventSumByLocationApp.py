from KafkaToConsoleApp import KafkaToConsoleApp
from pyspark.sql.functions import window, expr, to_json, struct
import time


class KafkaEventSumByLocationApp(KafkaToConsoleApp):
    """
    The KafkaEventSumByLocationApp:
    1. Reads records from a given Kafka topic
    2. Groups them by time window and location name, obtaining the aggregated sum of ammount
    3. Shows the result on the screen and then write it to the kafka topic sumByLocation.
    """

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        ts = time.localtime()
        print("Showing ordered batch: %s, at %s" % (batch_id, time.strftime("%Y-%m-%d %H:%M:%S", ts)))
        micro_batch_df.persist()
        kafka_df = micro_batch_df.orderBy(micro_batch_df["window.start"], micro_batch_df["locationName"]) \
            .withColumn("key", to_json(struct(micro_batch_df["window.start"], micro_batch_df["locationName"]))) \
            .withColumn("value", to_json(struct(micro_batch_df["window.start"],
                                                micro_batch_df["window.end"],
                                                micro_batch_df["sum(amount)"].alias("amountSum"),
                                                micro_batch_df["lat"],
                                                micro_batch_df["lon"],
                                                micro_batch_df["locationName"]))) \
            .select("key", "value")
        kafka_df.show(truncate=False)
        kafka_df.write \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("topic", "sumByLocation") \
            .save()
        micro_batch_df.unpersist()

    def get_locations(self):
        # The data of locations is a batch dataset
        return self.spark.read.option("header", True).option("inferschema", True).csv("./data/locations").cache()

    def get_events_df(self):
        locations_df = self.get_locations()

        # Fake locationId
        events_df = super().get_events_df()

        join_df = events_df.join(locations_df, events_df["locationId"] == locations_df["id"]) \
            .drop("id") \
            .withColumnRenamed("name", "locationName")

        # Group by window and location and sum amounts
        return join_df.groupBy(window(join_df["eventTimestamp"], "60 seconds"), join_df["locationName"],
                               join_df["lat"], join_df["lon"]).sum("amount")


if __name__ == '__main__':
    x = KafkaEventSumByLocationApp(processing_time="10 seconds")
    x.load(output_mode="update")
