from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Retail Intelligence System") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("data/sales.csv", header=True, inferSchema=True)

# Show data
df.show(5)
df.printSchema()
df.describe().show()