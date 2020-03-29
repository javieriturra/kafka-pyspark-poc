from RateToConsoleApp import RateToConsoleApp


class RateToKafkaApp(RateToConsoleApp):

    @staticmethod
    def write_micro_batch(micro_batch_df, batch_id):
        print("Writing batch: %s to kafka..." % batch_id)
        micro_batch_df.write \
            .format("kafka") \
            .option("checkpointLocation", "checkpoint") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("kafka.compression.type", "gzip") \
            .option("topic", "events") \
            .save()


if __name__ == '__main__':
    x = RateToKafkaApp()
    x.load()
