# Name: Haoran Zhu
# UNI: hz2712
from src.CSVDataTable import CSVDataTable
import os
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../Data/Baseball")


def tests_people():
    # Set up
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable(table_name="people", connect_info=connect_info, key_columns=["playerID"])
    print("tests_people()")

    # find_by_primary_key
    print("test find_by_primary_key()")
    print("test field_list is None")
    print(people.find_by_primary_key(key_fields=["affelje01"]))
    print("test field_list is not None")
    print(people.find_by_primary_key(key_fields=["affelje01"], field_list=["playerID", "birthYear", "birthMonth", "birthDay"]))
    print("test failed case: non-existent playerID; None should be returned")
    res = people.find_by_primary_key(key_fields=["nonexistent_key"])
    print("None is returned") if res is None else print("error: None is not returned")
    print()

    # find_by_template
    print("test find_by_template()")
    print("test field_list is None")
    print(people.find_by_template(template={"birthYear": "1979", "birthState": "AZ", "birthCity": "Phoenix"}))
    print("test field_list is not None")
    print(people.find_by_template(template={"birthYear": "1979", "birthState": "AZ", "birthCity": "Phoenix"},
                                  field_list=["playerID", "birthYear", "birthMonth", "birthDay"]))
    print("test failed case: non-existent template; empty list [] should be returned")
    print("returned:", people.find_by_template(template={"birthYear": "4000", "birthState": "XX", "birthCity": "Utopia"}))
    print()

    # delete_by_key
    print("test delete_by_key()")
    print("test successful deletion")
    print(people.delete_by_key(key_fields=["affelje01"]))
    print("check if deleted row is in the table...")
    res = people.find_by_primary_key(key_fields=["affelje01"])
    print("None is returned from find_by_primary_key(). The row is deleted.") if res is None else print("error: None is not returned")
    print("test failed deletion: non-existent playerID; 0 should be returned")
    print("returned:", people.delete_by_key(key_fields=["nonexistent_key"]))
    print()

    # insert
    print("test insert()")
    print("playerID affelje01 was deleted from delete_by_key tests. Insert player affelje01 back to the table...")
    people.insert(new_record={'playerID': 'affelje01', 'birthYear': '1979', 'birthMonth': '6', 'birthDay': '6',
                              'birthCountry': 'USA', 'birthState': 'AZ', 'birthCity': 'Phoenix', 'deathYear': '',
                              'deathMonth': '', 'deathDay': '', 'deathCountry': '', 'deathState': '', 'deathCity': '',
                              'nameFirst': 'Jeremy', 'nameLast': 'Affeldt', 'nameGiven': 'Jeremy David',
                              'weight': '225', 'height': '76', 'bats': 'L', 'throws': 'L', 'debut': '2002-04-06',
                              'finalGame': '2015-10-04', 'retroID': 'affej001', 'bbrefID': 'affelje01'})
    print("check if the inserted row is present in the table")
    res = people.find_by_primary_key(key_fields=["affelje01"])
    print("Returned value is not None. Insertion was successful.") if res is not None else print("insertion failed.")
    print()

    # delete_by_template
    print("test delete_by_template()")
    print("test successful deletion")
    print(people.delete_by_template(template={"birthYear": "1979", "birthState": "AZ", "birthCity": "Phoenix"}))
    print("check if deleted row is in the table...")
    res = people.find_by_template(template={"birthYear": "1979", "birthState": "AZ", "birthCity": "Phoenix"})
    print("0 row is returned from find_by_primary_template(). The row is deleted.") if len(res) == 0 else print(
        "error: some row is not returned")
    print("test failed deletion: non-existent template; 0 should be returned")
    print("returned:", people.delete_by_template(template={"birthYear": "4000", "birthState": "XX", "birthCity": "Utopia"}))
    print()

    # update_by_key
    print("test successful update")
    print(people.update_by_key(key_fields=["aardsda01"], new_values={"birthYear": "0000"}))
    print("print updated birthYear; 0000 should be returned")
    print("returned:", people.find_by_primary_key(key_fields=["aardsda01"], field_list=["birthYear"]))
    print("test failed update: nonexistent playerID; 0 should be returned")
    print("returned:", people.update_by_key(key_fields=["nonexistent_key"], new_values={"birthYear": "xxxx"}))
    print()

    # update_by_tenplate
    print("test successful update")
    print(people.update_by_template(template={"birthYear": "0000", "birthState": "CO", "birthCity": "Denver"},
                                    new_values={"birthYear": "1981"}))
    print("print updated birthYear; 1981 should be returned")
    print("returned:", people.find_by_template(template={"birthYear": "1981", "birthState": "CO", "birthCity": "Denver"},
                                               field_list=["birthYear"]))
    print("test failed update: nonexistent template; 0 should be returned")
    print("returned:", people.update_by_template(template={"birthYear": "4000", "birthState": "XX", "birthCity": "Utopia"},
                                               new_values={"birthYear": "1981"}))

    print("==========================================================================================================")


def tests_batting():
    # Set up
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    batting = CSVDataTable(table_name="batting", connect_info=connect_info, key_columns=["playerID",
                                                                                                 "yearID", "stint"])
    print("tests_batting()")

    # find_by_primary_key
    print("test find_by_primary_key()")
    print("test field_list is None")
    print(batting.find_by_primary_key(key_fields=["abercda01", "1871", "1"]))
    print("test field_list is not None")
    print(batting.find_by_primary_key(key_fields=["abercda01", "1871", "1"],
                                     field_list=["teamID", "lgID", "G", "AB"]))
    print("test failed case: non-existent playerID; None should be returned")
    res = batting.find_by_primary_key(key_fields=["nonexistent_key", "1871", "1"])
    print("None is returned") if res is None else print("error: None is not returned")
    print()

    # find_by_template
    print("test find_by_template()")
    print("test field_list is None")
    print(batting.find_by_template(template={"teamID": "ML1", "lgID": "NL", "G": "122", "AB": "468"}))
    print("test field_list is not None")
    print(batting.find_by_template(template={"teamID": "ML1", "lgID": "NL", "G": "122", "AB": "468"},
                                  field_list=["H", "2B", "3B", "HR"]))
    print("test failed case: non-existent template; empty list [] should be returned")
    print("returned:",
          batting.find_by_template(template={"teamID": "XXX", "lgID": "XX", "G": "122", "AB": "468"}))
    print()

    # delete_by_key
    print("test delete_by_key()")
    print("test successful deletion")
    print(batting.delete_by_key(key_fields=["abercda01", "1871", "1"]))
    print("check if deleted row is in the table...")
    res = batting.find_by_primary_key(key_fields=["abercda01", "1871", "1"])
    print("None is returned from find_by_primary_key(). The row is deleted.") if res is None else print(
        "error: None is not returned")
    print("test failed deletion: non-existent playerID; 0 should be returned")
    print("returned:", batting.delete_by_key(key_fields=["nonexistent_key", "1871", "1"]))
    print()

    # insert
    print("test insert()")
    print("batting [abercda01, 1871, 1] was deleted from delete_by_key tests. Insert the batting back to the table...")
    batting.insert(new_record={'playerID': 'abercda01', 'yearID': '1871', 'stint': '1', 'teamID': 'TRO', 'lgID': 'NA',
                               'G': '1', 'AB': '4', 'R': '0', 'H': '0', '2B': '0', '3B': '0', 'HR': '0', 'RBI': '0',
                               'SB': '0', 'CS': '0', 'BB': '0', 'SO': '0', 'IBB': '', 'HBP': '', 'SH': '',
                               'SF': '', 'GIDP': '0'})
    print("check if the inserted row is present in the table")
    res = batting.find_by_primary_key(key_fields=["abercda01", "1871", "1"])
    print("Returned value is not None. Insertion was successful.") if res is not None else print("insertion failed.")
    print()

    # delete_by_template
    print("test delete_by_template()")
    print("test successful deletion")
    print(batting.delete_by_template(template={"teamID": "ML1", "lgID": "NL", "G": "122", "AB": "468"}))
    print("check if deleted row is in the table...")
    res = batting.find_by_template(template={"teamID": "ML1", "lgID": "NL", "G": "122", "AB": "468"})
    print("0 row is returned from find_by_primary_template(). The row is deleted.") if len(res) == 0 else print(
        "error: some row is not returned")
    print("test failed deletion: non-existent template; 0 should be returned")
    print("returned:",
          batting.delete_by_template(template={"teamID": "XXX", "lgID": "XX", "G": "122", "AB": "468"}))
    print()

    # update_by_key
    print("test update_by_key()")
    print("test successful update")
    print(batting.update_by_key(key_fields=["abercda01", "1871", "1"], new_values={"AB": "27"}))
    print("print updated AB; 27 should be returned")
    print("returned:", batting.find_by_primary_key(key_fields=["abercda01", "1871", "1"], field_list=["AB"]))
    print("test failed update: nonexistent playerID; 0 should be returned")
    print("returned:", batting.update_by_key(key_fields=["nonexistent_key", "1871", "1"], new_values={"AB": "27"}))
    print()

    # update_by_template
    print("test update_by_template()")
    print("test successful update")
    print(batting.update_by_template(template={"teamID": "ML1", "lgID": "NL", "G": "153", "AB": "609"},
                                    new_values={"AB": "27"}))
    print("print updated AB; 27 should be returned")
    print("returned:",
          batting.find_by_primary_key(key_fields=["aaronha01", "1956", "1"], field_list=["AB"])
          )
    print("test failed update: nonexistent template; 0 should be returned")
    print("returned:",
          batting.update_by_template(template={"teamID": "ML1", "lgID": "NL", "G": "153", "AB": "000"},
                                    new_values={"AB": "27"}))

    print("==========================================================================================================")


def tests_appearances():
    # Set up
    connect_info = {
        "directory": data_dir,
        "file_name": "Appearances.csv"
    }
    appearances = CSVDataTable(table_name="appearances", connect_info=connect_info, key_columns=["yearID",
                                                                                                 "teamID", "playerID"])
    print("tests_appearances()")

    # find_by_primary_key
    print("test find_by_primary_key()")
    print("test field_list is None")
    print(appearances.find_by_primary_key(key_fields=["1871", "RC1", "addybo01"]))
    print("test field_list is not None")
    print(appearances.find_by_primary_key(key_fields=["1871", "RC1", "addybo01"],
                                      field_list=["G_all", "GS", "G_batting", "G_defense"]))
    print("test failed case: non-existent playerID; None should be returned")
    res = appearances.find_by_primary_key(key_fields=["1871", "RC1", "nonexistent_key"])
    print("None is returned") if res is None else print("error: None is not returned")
    print()

    # find_by_template
    print("test find_by_template()")
    print("test field_list is None")
    print(appearances.find_by_template(template={'playerID': "addybo01", 'G_all': '25', 'GS': '25', 'G_batting': '25'}))
    print("test field_list is not None")
    print(appearances.find_by_template(template={'playerID': "addybo01", 'G_all': '25', 'GS': '25', 'G_batting': '25'},
                                   field_list=["G_lf", "G_cf"]))
    print("test failed case: non-existent template; empty list [] should be returned")
    print("returned:",
          appearances.find_by_template(template={'G_all': '2s5', 'GS': '225', 'G_batting': '25d', 'G_defense': '125'}))
    print()

    # delete_by_key
    print("test delete_by_key()")
    print("test successful deletion")
    print(appearances.delete_by_key(key_fields=["1871", "RC1", "addybo01"]))
    print("check if deleted row is in the table...")
    res = appearances.find_by_primary_key(key_fields=["1871", "RC1", "addybo01"])
    print("None is returned from find_by_primary_key(). The row is deleted.") if res is None else print(
        "error: None is not returned")
    print("test failed deletion: non-existent playerID; 0 should be returned")
    print("returned:", appearances.delete_by_key(key_fields=["nonexistent_key", "RC1", "addybo01"]))
    print()

    # insert
    print("test insert()")
    print("appearance [nonexistent_key, RC1, addybo01] was deleted from delete_by_key tests. "
          "Insert the appearance back to the table...")
    appearances.insert(new_record={'yearID': '1871', 'teamID': 'RC1', 'lgID': 'NA', 'playerID': 'addybo01',
                                   'G_all': '25', 'GS': '25', 'G_batting': '25', 'G_defense': '25', 'G_p': '0',
                                   'G_c': '0', 'G_1b': '0', 'G_2b': '22', 'G_3b': '0', 'G_ss': '3', 'G_lf': '0',
                                   'G_cf': '0', 'G_rf': '0', 'G_of': '0', 'G_dh': '0', 'G_ph': '0', 'G_pr': '0'})
    print("check if the inserted row is present in the table")
    res = appearances.find_by_primary_key(key_fields=["1871", "RC1", "addybo01"])
    print("Returned value is not None. Insertion was successful.") if res is not None else print("insertion failed.")
    print()

    # delete_by_template
    print("test delete_by_template()")
    print("test successful deletion")
    print(appearances.delete_by_template(template={'playerID': "addybo01", 'G_all': '25', 'GS': '25', 'G_batting': '25'}))
    print("check if deleted row is in the table...")
    res = appearances.find_by_template(template={'playerID': "addybo01", 'G_all': '25', 'GS': '25', 'G_batting': '25'})
    print("0 row is returned from find_by_primary_template(). The row is deleted.") if len(res) == 0 else print(
        "error: some row is not returned")
    print("test failed deletion: non-existent template; 0 should be returned")
    print("returned:",
          appearances.delete_by_template(template={'playerID': "nonexistent_key", 'G_all': '25', 'GS': '25', 'G_batting': '25'}))
    print()

    # update_by_key
    print("test update_by_key()")
    print("test successful update")
    print(appearances.update_by_key(key_fields=["1871", "TRO", "abercda01"], new_values={"G_3b": "27"}))
    print("print updated G_3b; 27 should be returned")
    print("returned:", appearances.find_by_primary_key(key_fields=["1871", "TRO", "abercda01"], field_list=["G_3b"]))
    print("test failed update: nonexistent playerID; 0 should be returned")
    print("returned:", appearances.update_by_key(key_fields=["nonexistent_key", "1871", "1"], new_values={"G_3b": "27"}))
    print()

    # update_by_template
    print("test update_by_template()")
    print("test successful update")
    print(appearances.update_by_template(template={'playerID': "allisan01", 'G_all': '19', 'GS': '19', 'G_batting': '19'},
                                     new_values={"G_3b": "27"}))
    print("print updated G_3b; 27 should be returned")
    print("returned:",
          appearances.find_by_template(template={'playerID': "allisan01", 'G_all': '19', 'GS': '19', 'G_batting': '19'}
                                          ,field_list=["G_3b"])
          )
    print("test failed update: nonexistent template; 0 should be returned")
    print("returned:",
          appearances.update_by_template(template={'playerID': "nonexistent_key", 'G_all': '19', 'GS': '19', 'G_batting': '19'},
                                     new_values={"G_3b": "27"}))

    print("==========================================================================================================")


orig_stdout = sys.stdout
f = open("csv_table_tests.txt", "w+")
sys.stdout = f
tests_people()
tests_batting()
tests_appearances()
sys.stdout = orig_stdout
f.close()