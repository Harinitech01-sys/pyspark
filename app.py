
from pyspark.sql import SparkSession

# Step 1: Create a SparkSession
spark = SparkSession.builder \
    .appName("MyFirstPySparkApp") \
    .getOrCreate()

# Step 2: Create sample data
data = [
    (101, "Harini", "AI&DS", 95),
    (102, "Priya", "CSE", 88),
    (103, "Arun", "IT", 76)
]

# Step 3: Define column names
columns = ["id", "name", "department", "marks"]

# Step 4: Create a DataFrame
df = spark.createDataFrame(data, columns)

# Step 5: Display the DataFrame
df.show()

# Step 6: Stop Spark
spark.stop()
