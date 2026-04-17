import warnings
warnings.filterwarnings("ignore")

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Deployment").getOrCreate()

df = spark.read.csv("Vehicle_Sales_Data.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("vehicle_sales")

df1 = spark.sql("select * from vehicle_sales limit 10")
print(df1.show())


df2 = spark.sql("select * from vehicle_sales where Year=2012 limit 10")
print(df2.show())