from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


class Spark:
    """
    Utility class that wraps PySpark configuration and loading
    """

    def __init__(self):
        self.spark_ctx = SparkContext(
            conf=SparkConf()
            .set("spark.ui.port", "4051")
            .set("spark.executor.memory", "500M")
            .set("spark.driver.memory", "1G")
            .set("spark.driver.maxResultSize", "10G")
        )

        self.spark_ctx.setLogLevel("ERROR")
        self.spark = (
            SparkSession.builder.master("local[1]")
            .appName("football predictor")
            .getOrCreate()
        )
