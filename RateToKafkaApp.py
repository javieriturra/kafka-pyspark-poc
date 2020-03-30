from RateToConsoleApp import RateToConsoleApp
import time


class RateToKafkaApp(RateToConsoleApp):
    """
    The RateToConsoleApp reads records from a Apache Spark rate (fake) stream and writes them to an Apache Kafka topic.
    Useful to emulate events and send them to Kafka.
    """

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        ts = time.localtime()
        print("Writting batch %s to kafka, at %s" % (batch_id, time.strftime("%Y-%m-%d %H:%M:%S", ts)))
        micro_batch_df.show(truncate=False)
        micro_batch_df.write \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("topic", "events") \
            .save()


if __name__ == '__main__':
    x = RateToKafkaApp(processing_time="5 seconds")
    x.load("append")
