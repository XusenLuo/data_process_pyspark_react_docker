'''
Created on Aug 7, 2026

@author: Loosoon

Define all the settings of the project
Includes: input and output path
'''

# rating_dir = "input_data/u.data"
# movie_dir = "input_data/u.item"
#
# output_dir = "output/movie_ranking_list.csv"
# json_dir = "output/movie_list.json"


from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "backend" / "src" / "input_data"

OUTPUT_DIR = PROJECT_ROOT / "backend" / "output"

FRONTEND_DATA_DIR = (
    PROJECT_ROOT / "frontend" / "src" / "data"
)

DATA_FILE = DATA_DIR / "u.data"

ITEM_FILE = DATA_DIR / "u.item"

RANKING_OUTPUT = (
    OUTPUT_DIR / "movie_ranking_list.csv"
)

MOVIE_JSON_OUTPUT = (
    FRONTEND_DATA_DIR / "movie_list.json"
)