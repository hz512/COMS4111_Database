from src.CSVDataTable import CSVDataTable

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../Data/Baseball")


def tests_people():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }


def tests_batting():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }


def tests_appearances():
    connect_info = {
        "directory": data_dir,
        "file_name": "Appearances.csv"
    }


tests_people()

tests_batting()

tests_appearances()
