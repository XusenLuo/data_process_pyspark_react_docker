'''
Created on Aug 7, 2026

@author: Loosoon

Define all the functions to load input data
'''



def read_ratings(spark, rating_dir):
    """
    TO read the ratings data.
    Args:
      spark: a SparkSession
      rating_dir: a str of data path
      
    Return: pyspark.sql.DataFrame
    """
    
    ratings = spark.read.csv(rating_dir, sep="\t", inferSchema=True)
    
    #define the column names
    ratings = ratings.toDF("user_id","movie_id","rating","timestamp")
    
    ratings.show()
    print(ratings.dtypes)
    return ratings


def read_movies(spark, movie_dir):
    """
    TO read the movies data.
    Args:
      spark: a SparkSession
      movie_dir: a str of data path
      
    Return: pyspark.sql.DataFrame
    """
    
    movies = spark.read.csv(movie_dir, sep="|", inferSchema=True, encoding="ISO-8859-1")
    
    #define the column names
    movies = movies.toDF("movie_id","movie_title","release_date",
                         "video_release_date","IMDb_URL","unknown","Action",
                         "Adventure","Animation","Children","Comedy","Crime",
                         "Documentary","Drama","Fantasy","Film_Noir","Horror",
                         "Musical","Mystery","Romance","Sci_Fi","Thriller","War",
                         "Western")
    movies.show()
    print(movies.dtypes)
    return movies