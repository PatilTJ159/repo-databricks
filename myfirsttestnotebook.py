from pyspark.sql import SparkSession


def some_function(x):
    return x * 2

def get_spark_session():
    return spark = SparkSession.builder.getOrCreate()

# Databricks notebook source
def run_spark_job():
    spark = get_spark_session()
    data = spark.range(1, 10).toDF("number")
    data.filter("number % 2 == 0").show()

if __name__ == "__main__":
    run_spark_job()
