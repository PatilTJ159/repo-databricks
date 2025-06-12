# myfirst_test_notebook.py

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()

def some_function(x):
    return x * 2  # Example function to test

def run_job():
    data = spark.range(1, 10).toDF("number")
    data.filter("number % 2 == 0").show()

if __name__ == "__main__":
    run_job()
