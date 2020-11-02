Name: Haoran Zhu
UNI: hz2712

find_by_primary_key:
   - Error handling: if the length of input key_fields does not match the length of key_columns,
   print an error message and terminate the execution.
   - Explanation of codes: iterate through the table row by row and find the row with the same primary key
   as the input key_fields. If there is a specified field_list, then project the field_list onto the row.
   If field_list is None, then simply return the entire row. If we failed to find the matching row, then
   None is returned.

find_by_template:
    - Error handling: if the input template contain a column name that does not appear in the table,
    print an error message about invalid column name and terminate the execution. An empty list is returned.
    - Explanation of codes: iterate through the table row by row and find row(s) with the same attribute values as
    ones in the template. Every time a candidate row is found, it's appended into a list. If there is a specified
    field_list, then project the field_list onto the row(s). Otherwise, row(s) remains unchanged. The list with
    matching row(s) is returned. If there are no matching rows, an empty list is returned.

delete_by_key:
    - Error handling: if the length of input key_fields does not match the length of key_columns,
   print an error message and terminate the execution.
   - Explanation of codes: iterate through the table row by row and find the row with the same primary key
   as the input key_fields. If such a row is found, remove it from the table it and return 1. Otherwise, return 0.

delete_by_template:
    - Error handling: if the input template contain a column name that does not appear in the table,
    print an error message about invalid column name and terminate the execution. 0 is then returned.
    - Explanation of codes: iterate through the table row by row and find row(s) with the same attribute values as
    ones in the template. Every time a candidate row is found, increment the counter by 1 and append the index of the
    candidate row into a list. Then use the indices list to remove row(s) from the table. The counter (which represents
    the number of deleted rows) is returned.

update_by_key:
    - Error handling: if the length of input key_fields does not match the length of key_columns,
   print an error message and terminate the execution. Also, if the input new_values contains a column name that does
   not appear in the table, print an error message about invalid column and terminate the execution. In either case,
   0 is returned.
   - Explanation of codes: iterate through the table row by row and find the row with the same primary key
   as the input key_fields. If such a row is found, update it according to new_values. Then return 1. If no such
   row is found, 0 is returned.

update_by_template:
    - Error handling: if the input template or new_values contains a column name that does not appear in the table,
    print an error message about invalid column and terminate the execution. 0 is then returned.
    - Explanation of codes: iterate through the table row by row and find row(s) with the same attribute values as
    ones in the template. Every time a candidate row is found, increment the counter by 1 and update the candidate row
    according to new_values. The counter (which represents the number of updated rows) is returned.

insert:
    - Error handling: if the input new_record does not contain all column names in the table, an error message is printed
    about the missing attribute(s). In this case, no insertion is performed.
    - Explanation of codes: since we need to make sure the new row has the same order of attributes as other rows
    in the table, an OrderedDict is used instead of an ordinary dict, which does not impose ordering to its pairs.
    Iterate through the column names in the table (in order), and for every column name, find the corresponding pair in
    new_record and append the tuple (field, value) into a list. List was used because it preserves the ordering of its
    element. Then an OrderedDict is constructed based on that list and eventually appended into the table.