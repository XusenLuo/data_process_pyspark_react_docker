'''
Created on Aug 7, 2026

@author: Loosoon

The main function of this project.
Run this function to start.
'''

from pyspark.sql import SparkSession

from config import (
    DATA_FILE,
    ITEM_FILE,
    RANKING_OUTPUT,
    MOVIE_JSON_OUTPUT
)

from data_loader import (
    read_ratings,
    read_movies
)

from data_processor import (
    movie_ranking, 
    export_movie_ranking, 
    export_movie_json
)


def main():

    spark = (SparkSession.builder.appName("MovieRanking").getOrCreate())
    ratings = read_ratings(spark, str(DATA_FILE))
    movies = read_movies(spark, str(ITEM_FILE))
    
    sp_df = movie_ranking(spark, ratings, movies)
    
    export_movie_ranking(sp_df, str(RANKING_OUTPUT))
    export_movie_json(sp_df, str(MOVIE_JSON_OUTPUT))
    

    print(f"\nOutput saved to: {RANKING_OUTPUT}")
    print(f"Exported 10 movie records to: {MOVIE_JSON_OUTPUT}")


if __name__ == "__main__":
    main()





