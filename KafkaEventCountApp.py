from KafkaToConsoleApp import KafkaToConsoleApp
from pyspark.sql.functions import window
import time


class KafkaEventCountApp(KafkaToConsoleApp):
    """
    The KafkaEventCountApp reads records from a Kafka topic, groups by time window and shows the result on the screen
    """

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        ts = time.localtime()
        print("Showing batch: %s, at %s" % (batch_id, time.strftime("%Y-%m-%d %H:%M:%S", ts)))
        micro_batch_df.orderBy(micro_batch_df["window.start"]).show(truncate=False)

    def get_events_df(self):
        events_df = super().get_events_df()
        count_df = events_df.groupBy(window(events_df["eventTimestamp"], "60 seconds")).count()
        return count_df


if __name__ == '__main__':
    x = KafkaEventCountApp(processing_time="10 seconds")
    x.load("complete")
