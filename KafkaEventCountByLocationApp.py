from KafkaToConsoleApp import KafkaToConsoleApp
from pyspark.sql.functions import window, expr
import time


class KafkaEventCountByLocationApp(KafkaToConsoleApp):
    """
    The KafkaEventCountByLocationApp reads records from a given Kafka topic, groups by time window and location name
    and shows the result on the screen. The data of locations is a batch dataset, joined with the streaming data.
    """

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        ts = time.localtime()
        print("Showing ordered batch: %s, at %s" % (batch_id, time.strftime("%Y-%m-%d %H:%M:%S", ts)))
        micro_batch_df.orderBy(micro_batch_df["window.start"], micro_batch_df["locationName"]).show(truncate=False)

    def get_locations(self):
        locations_df = self.spark.read.option("header", True).option("inferschema", True).csv("./data/locations")
        return locations_df.cache()  # Very small dataframe, it can be cached

    def get_events_df(self):
        locations_df = self.get_locations()

        # Fake locationId
        events_df = super().get_events_df().withColumn("locationId", expr("eventValue % 3 + 1 "))

        join_df = events_df.join(locations_df, events_df["locationId"] == locations_df["id"]) \
            .drop("id") \
            .withColumnRenamed("name", "locationName")

        # Group by window and location
        return join_df.groupBy(window(join_df["eventTimestamp"], "60 seconds"), join_df["locationName"]).count()


if __name__ == '__main__':
    x = KafkaEventCountByLocationApp(processing_time="10 seconds")
    x.load("update")
