#Program to use mysql library.
import mysql.connector
import time
connection = mysql.connector.connect(user = "Saikrishna", password = "Saikrishna", host = "165.22.14.77", database = "dbSaikrishna");
cursor = connection.cursor(prepared = True)
print("Welcome to the MySQL monitor.  Commands end with ; or \\g.")
print("Your MySQL connection id is " + str(connection.connection_id))
print("Server version: 5.7.32-0ubuntu0.18.04.1 (Ubuntu)")
print("\nCopyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.")
print("\nOracle is a registered trademark of Oracle Corporation and/or its")
print("affiliates. Other names may be trademarks of their respective")
print("owners.")
print("\nType 'help;' or '\\h' for help. Type '\\c' to clear the current input statement.\n")

def find_columns_length():
    columns_length = []
    for fields_index in range(len(field_names)):
        field_name_length = len(field_names[fields_index])
        for values_index in range(len(field_values)):
            field_value_length = len(str(field_values[values_index][fields_index]))
            if field_name_length < field_value_length:
                field_name_length = field_value_length
            elif fields_index == len(field_names):
                break
        columns_length.append(field_name_length)
    return columns_length

def print_border(max_length_of_column):
    for counter in range(len(field_names)):
        print('+', end = "")
        print('-' * (max_length_of_column[counter] + 2), end = "")
    print('+')

def print_column_headings(max_length_of_column):
    for counter in range(len(field_names)):
        print('|', end = " ")
        print(field_names[counter], end = " ")
        print(' ' * (max_length_of_column[counter] - len(field_names[counter])), end = "")
    print('|')

def print_column_values(max_length_of_column):
    for values_index in range(len(field_values)):
        for fields_index in range(len(field_names)):
            field_value = field_values[values_index][fields_index]
            print('|', end = " ")
            print(field_value, end = " ")
            print(' ' * (max_length_of_column[fields_index] - len(str(field_value))), end = "")
        print('|')          

def print_column_values_in_tabular_format():
    max_length_of_column = find_columns_length()
    print_border(max_length_of_column)
    print_column_headings(max_length_of_column)
    print_border(max_length_of_column)
    print_column_values(max_length_of_column)
    print_border(max_length_of_column)

def print_no_of_rows(no_of_rows):
    if no_of_rows == 0:
        print("Empty ", end = "")
    else:
        print_column_values_in_tabular_format()
        print(str(no_of_rows) + " rows in ", end = "")

def print_time_taken(final_time):
    print("set (" + str(final_time) + " sec)")

while True:
    query = input("mysql> ")
    cursor = connection.cursor()
    if query.lower() == 'quit' or query.lower() == 'exit':
        connection.close()
        print("Bye")
        exit()
    else:
        try:
            start_time = time.time()
            cursor.execute(query)
            if query[:3].lower() == 'use':
                print("Database changed")
        except:
            print("You have an error in your SQL syntax;")
            continue
        if query[:4].lower() == 'show' or query[:6].lower() == 'select':
            field_names = [description[0] for description in cursor.description]
            field_values = []
            for field_value in cursor:
                field_value = list(field_value)
                field_values.append(field_value)
            end_time = time.time()
            no_of_rows = len(field_values)
            final_time = round(end_time - start_time, 2)
            print_no_of_rows(no_of_rows)
            print_time_taken(final_time)
            print()
