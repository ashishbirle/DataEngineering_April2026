import warnings
warnings.filterwarnings("ignore")

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Deployment").getOrCreate()

df_csv = spark.read.csv("Vehicle_Sales_Data.csv", header=True, inferSchema=True)

df_csv.createOrReplaceTempView("vehicle_sales")

df1 = spark.sql("select * from vehicle_sales limit 10")
print(df1.show())

data = [
    (1, "Ashok", 25),
    (2, "Ravi", 30),
    (3, "Priya", 28),
    (4, "Neha", 24),
    (5, "Amit", 27)
]

# Defining column names
columns = ["id", "name", "age"]

# Create DataFrame
df_new = spark.createDataFrame(data, columns)

# Show DataFrame
print(df_new.show())