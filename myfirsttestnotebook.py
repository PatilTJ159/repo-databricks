from pyspark.sql import SparkSession

def some_function(x):
    return x * 2
  
spark = SparkSession.builder.getOrCreate()
# Databricks notebook source
data = spark.range(1, 10).toDF("number")
data.filter("number % 2 == 0").show()
