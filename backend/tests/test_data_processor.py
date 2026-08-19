'''
Created on Aug 8, 2026

@author: Loosoon

Unit test
'''
import os
import unittest
import tempfile

import pandas as pd
from pyspark.sql import SparkSession

from data_processor import export_movie_ranking

"""
To test export_movie_ranking() function
"""
class TestMovieExport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Create SparkSession once before all tests.
        """
        cls.spark = (
            SparkSession.builder
            .master("local[2]")
            .appName("MovieRankingTest")
            .getOrCreate()
        )

    @classmethod
    def tearDownClass(cls):
        """
        Stop SparkSession after all tests.
        """
        cls.spark.stop()

    def test_export_movie_ranking(self):
        # Arrange
        data = [
            (1, 101, "The Matrix", 4.3),
            (2, 102, "Inception", 2.7),
            (3, 103, "Titanic", 3.5 )
        ]

        columns = [
            "Rank",
            "movie_id",
            "movie_title",
            "avg_rating"
        ]

        spark_df = self.spark.createDataFrame(
            data,
            columns
        )

        # Create temporary output file
        with tempfile.TemporaryDirectory() as temp_dir:

            output_file = os.path.join(
                temp_dir,
                "movie_ranking.csv"
            )

            # Act
            export_movie_ranking(
                spark_df,
                output_file
            )

            # Assert: file exists
            self.assertTrue(
                os.path.exists(output_file)
            )

            # Read exported CSV
            actual = pd.read_csv(output_file)

            # Expected DataFrame
            expected = pd.DataFrame({
                "Rank": [1, 2, 3],
                "movie_id": [101, 102, 103],
                "movie_title": [
                    "The Matrix",
                    "Inception",
                    "Titanic"
                ],
                "avg_rating": [4.3, 2.7, 3.5]
            })

            # Check entire DataFrame
            pd.testing.assert_frame_equal(
                actual,
                expected
            )


if __name__ == "__main__":
    unittest.main()    
    
    
