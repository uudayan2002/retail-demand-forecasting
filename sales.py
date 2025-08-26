from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, avg, max, min, to_date, year, month

print("Starting SparkSession...")
spark = SparkSession.builder \
    .appName("Sales Data Analysis") \
    .getOrCreate()
print("SparkSession started.")

df = spark.read.csv("sales_dataset.csv", header=True, inferSchema=True)
df.show(5)
df.printSchema()

df = df.withColumn("OrderDate", to_date(col("OrderDate"), "dd-MM-yyyy")) \
       .withColumn("ShipDate", to_date(col("ShipDate"), "dd-MM-yyyy"))
# df.groupBy().agg(sum("Sales").alias("TotalSales")).show()
# df.groupBy("Category").agg(sum("Sales").alias("TotalSales")).orderBy(col("TotalSales").desc()).show()
# df.groupBy("Region").agg(sum("Sales").alias("TotalSales")).orderBy(col("TotalSales").desc()).show()p