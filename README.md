# pyspark-movie-reviews

PySpark script to load, clean, and analyze the IMDb 50K movie review dataset.

## Dataset

[IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) (Kaggle)

Downloaded using `download_data.py` (uses `kagglehub`).

## What the script does

`main.py`:

1. Loads the CSV into a Spark DataFrame
2. Prints the schema and first 5 rows
3. Removes any rows with null/empty reviews
4. Counts total reviews and the positive/negative split
5. Adds a `review_length` column (character count)
6. Filters reviews longer than 500 characters
7. Saves the cleaned/transformed data to `cleaned_reviews_output/`

## Running it

```bash
pip3 install kagglehub pyspark
python3 download_data.py
python3 main.py
```

## Notes

- Dataset: 50,000 reviews, 25,000 positive / 25,000 negative
- No null/empty reviews found after cleaning (dataset was already clean)
- CSV reading needs `quote`, `escape`, and `multiLine` options set, otherwise Spark splits reviews containing quotes into the wrong columns