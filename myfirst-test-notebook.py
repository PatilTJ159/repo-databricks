from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
# Databricks notebook source
data = spark.range(1, 10).toDF("number")
data.filter("number % 2 == 0").show()
