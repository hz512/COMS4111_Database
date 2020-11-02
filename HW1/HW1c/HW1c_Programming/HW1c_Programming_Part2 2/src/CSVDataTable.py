# Name: Haoran Zhu
# UNI: hz2712
from src.BaseDataTable import BaseDataTable
from collections import OrderedDict
import copy
import logging
import json
import os
import pandas as pd
import csv

pd.set_option("display.width", 256)
pd.set_option('display.max_columns', 20)

# You can change to wherever you want to place your CSV files.
rel_path = os.path.realpath('./Data')


class CSVDataTable(BaseDataTable):
    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. with extend the
    base class and implement the abstract methods.
    """
    _rows_to_print = 10
    _no_of_separators = 2

    def __init__(self, table_name, connect_info, key_columns, debug=True, load=True, rows=None):

        """
        :param table_name: Logical name of the table.
        :param connect_info: Dictionary of parameters necessary to connect to the data.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
        """
        self._data = {
            "table_name": table_name,
            "connect_info": connect_info,
            "key_columns": key_columns,
            "debug": debug
        }

        self._key_columns = key_columns

        self._logger = logging.getLogger()

        self._logger.debug("CSVDataTable.__init__: data = " + json.dumps(self._data, indent=2))


        if rows is not None:
            self._rows = copy.copy(rows)
        else:
            self._rows = []
            self._load()

    def __str__(self):

        result = "CSVDataTable: config data = \n" + json.dumps(self._data, indent=2)

        no_rows = len(self._rows)
        if no_rows <= CSVDataTable._rows_to_print:
            rows_to_print = self._rows[0:no_rows]
        else:
            temp_r = int(CSVDataTable._rows_to_print / 2)
            rows_to_print = self._rows[0:temp_r]
            keys = self._rows[0].keys()

            for i in range(0, CSVDataTable._no_of_separators):
                tmp_row = {}
                for k in keys:
                    tmp_row[k] = "***"
                rows_to_print.append(tmp_row)

            rows_to_print.extend(self._rows[int(-1 * temp_r) - 1:-1])

        df = pd.DataFrame(rows_to_print)
        result += "\nSome Rows: = \n" + str(df)

        return result

    def _add_row(self, r):
        if self._rows is None:
            self._rows = []
        self._rows.append(r)

    def _load(self):

        dir_info = self._data["connect_info"].get("directory")
        file_n = self._data["connect_info"].get("file_name")
        full_name = os.path.join(dir_info, file_n)

        with open(full_name, "r") as txt_file:
            csv_d_rdr = csv.DictReader(txt_file)
            for r in csv_d_rdr:
                self._add_row(r)

        self._logger.debug("CSVDataTable._load: Loaded " + str(len(self._rows)) + " rows")

    def save(self):
        """
        Write the information back to a file.
        :return: None
        """
        fn = rel_path + "/" + self.table_file
        with open(fn, "w") as csvfile:
            csvw = csv.DictWriter(csvfile, self.columns)
            csvw.writeheader()
            for r in self._rows:
                csvw.writerow(r)

    def get_key_column(self):
        pkey = self._data.get("key_columns")
        return pkey

    @staticmethod
    def _project(row, field_list):

        result = {}

        if field_list is None:
            return row

        for f in field_list:
            result[f] = row[f]

        return result

    @staticmethod
    def matches_template(row, template):

        result = True
        if template is not None:
            for k, v in template.items():
                if v != row.get(k, None):
                    result = False
                    break

        return result

    def find_by_primary_key(self, key_fields, field_list=None):
        """

        Returns a record that matches the primary key.
        :param key_fields: The list with the values for the key_columns, in order, to use to find a record.
        :param field_list: A subset of the fields of the record to return.
        :return: None, or a dictionary containing the requested fields for the record identified
            by the key.

        """
        if len(key_fields) != len(self._key_columns):
            print("Length of key_fields does not match the length of key columns")
            return None
        ret = {}
        for row in self._rows:
            flag = True
            for i in range(len(key_fields)):
                if row[self._key_columns[i]] != key_fields[i]:
                    flag = False
                    break
            if flag:
                if field_list is not None:
                    for f in field_list:
                        ret[f] = row[f]
                    return ret
                return dict(row)
        return None


    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """

        Returns a record that matches the template.
        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}
        :param field_list: A list of request fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A list containing dictionaries. A dictionary is in the list representing each record
            that matches the template. The dictionary only contains the requested fields.

        """
        ret = []
        for row in self._rows:
            flag = True
            for field, value in template.items():
                if field not in row:
                    print("invalid column name: " + str(field))
                    return []
                if row[field] != value:
                    flag = False
                    break
            if flag:
                if field_list is not None:
                    d = {}
                    for f in field_list:
                        d[f] = row[f]
                    ret.append(d)
                else:
                    ret.append(dict(row))
        return ret


    def delete_by_key(self, key_fields):
        """

        Deletes the record that matches the key.
        :param key_fields: List of value for the key fields.
        :return: A count of the rows deleted.

        """
        if len(key_fields) != len(self._key_columns):
            print("Length of key_fields does not match the length of key columns")
            return 0
        for i in range(len(self._rows)):
            row, flag = self._rows[i], True
            for j in range(len(key_fields)):
                if row[self._key_columns[j]] != key_fields[j]:
                    flag = False
                    break
            if flag:
                self._rows.pop(i)
                return 1
        return 0


    def delete_by_template(self, template):
        """

        Deletes the record that matches the template.
        :param template: Template to determine rows to delete.
        :return: Number of rows deleted.
        """
        cnt, indices, n = 0, [], len(self._rows)
        for i in range(n):
            row, flag = self._rows[i], True
            for field, value in template.items():
                if field not in row:
                    print("invalid column name: " + str(field))
                    return 0
                if row[field] != value:
                    flag = False
                    break
            if flag:
                indices.append(i)
                cnt += 1
        if len(indices) == 0:
            return 0
        for i in range(len(indices) - 1, -1, -1):
            self._rows.pop(indices[i])
        return cnt


    def update_by_key(self, key_fields, new_values):
        """

        Updates the record that matches the key.
        :param key_fields: List of value for the key fields.
        :param new_values: A dict of field:value to set for updated row.
        :return: Number of rows updated.
        """

        if len(key_fields) != len(self._key_columns):
            print("Length of key_fields does not match the length of key columns")
            return 0
        for i in range(len(self._rows)):
            flag, row = True, self._rows[i]
            for j in range(len(key_fields)):
                if row[self._key_columns[j]] != key_fields[j]:
                    flag = False
                    break
            if flag:
                for field, value in new_values.items():
                    if field not in row:
                        print("invalid column name: " + str(field))
                        return 0
                    self._rows[i][field] = value
                return 1
        return 0


    def update_by_template(self, template, new_values):
        """

        Updates the record that matches the template.
        :param template: Template for rows to match.
        :param new_values: New values to set for matching fields.
        :return: Number of rows updated.
        """
        cnt = 0
        for i in range(len(self._rows)):
            flag, row = True, self._rows[i]
            for field, value in template.items():
                if field not in row:
                    print("invalid column name: " + str(field))
                    return 0
                if row[field] != value:
                    flag = False
                    break
            if flag:
                cnt += 1
                for f, v in new_values.items():
                    if f not in row:
                        print("invalid column name: " + str(f))
                        return 0
                    self._rows[i][f] = v
        return cnt


    def insert(self, new_record):
        """

        Inserts a new record.
        :param new_record: A dictionary representing a row to add to the set of records.
        :return: None
        """
        keys, newRow = self._rows[0].keys(), []
        for k in keys:
            if k not in new_record:
                print("missing column name: " + str(k))
                return
            newRow.append((k, new_record[k]))
        self._rows.append(OrderedDict(newRow))


    def get_rows(self):
        return self._rows
