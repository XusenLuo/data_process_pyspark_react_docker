'''
Created on Aug 7, 2026

@author: Loosoon

To define the main logic of ranking movies.
'''

from pyspark.sql.functions import array, when, col, expr
import json


# List of all the genres
genre_columns = [
    "Action", "Adventure", "Animation", "Children",
    "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
    "Film_Noir", "Horror", "Musical", "Mystery", "Romance",
    "Sci_Fi", "Thriller", "War", "Western"
]

genre_expressions = ", ".join(
    f"CASE WHEN `{genre}` = 1 THEN '{genre}' END"
    for genre in genre_columns
)

def movie_ranking(spark, ratings, movies):
    """
    TO rank movies, keep the top 100.
    Args:
      spark: a SparkSession
      ratings: rating data, pyspark.sql.DataFrame
      movies: movies data, pyspark.sql.DataFrame
      
    Return:
      pyspark.sql.DataFrame
    """

    # create two temporary table views in Spark session
    # So that we can write SQL to process the data
    ratings.createOrReplaceTempView("ratings_detail")
    movies.createOrReplaceTempView("movies_info")
    
    # Firstly, calculate the average rating and number of ratings
    # Secondly, use row_number() to generate the rankings
    # Finally, join with movie_info to get other columns
    sql = r"""
    select 
      a.Rank,
      a.movie_id,
      b.movie_title,
      a.avg_rating,
      a.cnt_rating,
      b.Action, b.Adventure, b.Animation, b.Children, 
      b.Comedy, b.Crime, b.Documentary, b.Drama, b.Fantasy, 
      b.Film_Noir, b.Horror, b.Musical, b.Mystery, b.Romance, 
      b.Sci_Fi, b.Thriller, b.War, b.Western
    from (
      select 
        row_number() over(order by avg_rating desc) as Rank,
        movie_id,
        avg_rating,
        cnt_rating
      from (
        select 
          movie_id,
          avg(rating) as avg_rating,
          count(rating) as cnt_rating
        from ratings_detail
        group by movie_id
      )t
    )a 
    left join (
      select 
        movie_id, movie_title,
        Action, Adventure, Animation, Children, 
        Comedy, Crime, Documentary, Drama, Fantasy, 
        Film_Noir, Horror, Musical, Mystery, Romance, 
        Sci_Fi, Thriller, War, Western
      from movies_info
    )b on a.movie_id=b.movie_id
    limit 100
    """
    result = spark.sql(sql)
        
    result.show()
    print(result.dtypes)
    
    return result


def export_movie_ranking(spark_df, output_dir):
    """
    TO export a csv file of movie rankings.
    Args:
      spark_df: pyspark.sql.DataFrame
      output_dir: a string of output path
    """
    
    # Only export target columns
    spark_df_sel = spark_df.select(["Rank", "movie_id", "movie_title", "avg_rating"])
    
    pd_df = spark_df_sel.toPandas()
    pd_df.to_csv(output_dir,index=False, header=True)
    

def export_movie_json(spark_df, json_dir):
    """
    TO export a josn file of 10 movie rankings
    for the web view.
    Args:
      spark_df: pyspark.sql.DataFrame
      json_dir: a string of output path
    """
    
    # Only use 10 records
    spark_df = spark_df.limit(10)
    # Convert columns of genres into an array 
    spark_df = spark_df.withColumn("genres", 
                               expr(f"""
                               filter(array({genre_expressions}), 
                                x -> x IS NOT NULL)""")
                               )
    
    spark_df = spark_df.select(col("movie_id"), col("movie_title"), 
                                    col("cnt_rating"), col("avg_rating"),
                                    col("genres"))
    data = spark_df.collect()
    with open(json_dir, "w", encoding="utf-8") as f:
        json.dump(
            [row.asDict() for row in data],
            f,
            ensure_ascii=False,
            indent=2
        )
    
    
    
    
        

