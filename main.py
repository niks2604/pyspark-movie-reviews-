from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IMDbReviews").getOrCreate()

path = "/Users/aniks/.cache/kagglehub/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews/versions/1/IMDB Dataset.csv"
df = spark.read.csv(
    path,
    header=True,
    inferSchema=True,
    quote='"',
    escape='"',
    multiLine=True
)

df.printSchema()
df.show(5)

from pyspark.sql.functions import col, trim

# Task: Clean the data — remove rows with null or empty reviews
df_clean = df.filter(
    col("review").isNotNull() & (trim(col("review")) != "")
)

print("Rows before cleaning:", df.count())
print("Rows after cleaning:", df_clean.count())

# Task: Analyze the data
total_reviews = df_clean.count()
print("Total reviews:", total_reviews)

df_clean.groupBy("sentiment").count().show()

from pyspark.sql.functions import length

# Task: Transform the data
df_clean = df_clean.withColumn("review_length", length(col("review")))

df_clean.select("review", "review_length").show(5, truncate=50)

long_reviews = df_clean.filter(col("review_length") > 500)
print("Reviews longer than 500 characters:", long_reviews.count())
long_reviews.select("review", "review_length").show(5, truncate=50)

# Task: Save Your Results
output_path = "cleaned_reviews_output"
df_clean.write.csv(output_path, header=True, mode="overwrite")

print("Saved cleaned data to:", output_path)