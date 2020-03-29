mkdir -p jars

wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.11/2.4.5/spark-sql-kafka-0-10_2.11-2.4.5.jar --directory-prefix jars/
wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.11/2.4.5/spark-streaming-kafka-0-10_2.11-2.4.5.jar --directory-prefix jars/
wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.jar --directory-prefix jars/

DEST_DIR=$HOME/anaconda3/envs/pyspark-env/lib/python3.7/site-packages/pyspark

cp jars/*jar ${DEST_DIR}/jars/

ls -l $HOME/anaconda3/envs/pyspark-env/lib/python3.7/site-packages/pyspark/jars/*kafka*

