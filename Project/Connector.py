#########################################################################################################################
#########################################################################################################################
## Project: Class for default database connection and interaction with MySQL database.                                 ##
##                                                                                                                     ##
## Autor: Ryan Junge                                                                                                   ##
## Date: 2023-09-28                                                                                                    ##
## Version: 1.0                                                                                                        ##
##                                                                                                                     ##
## Description: This class provides methods for connecting to and interacting with a MySQL database.                   ##
##                                                                                                                     ##
## Usage:                                                                                                              ##
##   from connector import DatabaseConnector                                                                           ##
##                                                                                                                     ##
##   # Create a database connector object                                                                              ##
##   db = DatabaseConnector(host, user, password, database)                                                            ##
##                                                                                                                     ##
##   host = "localhost"                                                                                                ##
##   user = "root"                                                                                                     ##
##   password = ""                                                                                                     ##
##   database = "test"                                                                                                 ##
##                                                                                                                     ##
##   # Connect to the database                                                                                         ##
##   db.connect()                                                                                                      ##
##                                                                                                                     ##
##   # Create a table                                                                                                  ##
##   table_name = "test_table"                                                                                         ##
##   columns = ["id INT AUTO_INCREMENT PRIMARY KEY", "name VARCHAR(255) NOT NULL"]                                     ##
##   db.create_table(table_name, columns)                                                                              ##
##                                                                                                                     ##
##   # Insert data into the table                                                                                      ##
##   columns = ["name"]                                                                                                ##
##   values = ["John"]                                                                                                 ##
##   db.insert_data(table_name, columns, values)                                                                       ##
##                                                                                                                     ##
##   # Fetch the results of the query                                                                                  ##
##
##   results = db.fetch_all()                                                                                          ##
##                                                                                                                     ##
##   # Close the database connection                                                                                   ##
##   db.close()                                                                                                        ##
##                                                                                                                     ##
##                                                                                                                     ##
#########################################################################################################################
#########################################################################################################################


import mysql.connector

class DatabaseConnector:
    """
    This class provides methods for connecting to and interacting with a MySQL database.
    """

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = None
        self.cursor =  None

    def connect(self):
        """
        Connect to the MySQL database.
        """
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.mydb.cursor(buffered=True)
        except mysql.connector.Error as err:
            raise  # Rethrow the exception to handle it at a higher level

    def close(self):
        """
        Close the database connection.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.mydb:
                self.mydb.close()
        except mysql.connector.Error as err:
            raise  # Rethrow the exception to handle it at a higher level

    def execute(self, query):
        """
        Execute a SQL query.
        """
        try:
            self.cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level

    def fetch_all(self):
        """
        Fetch all rows from the last executed query.
        """
        return self.cursor.fetchall()

    def fetch_one(self):
        """
        Fetch the next row from the last executed query.
        """
        return self.cursor.fetchone()

    def fetch_many(self, size):
        """
        Fetch a specified number of rows from the last executed query.
        """
        return self.cursor.fetchmany(size)

    def create_table(self, table_name, columns):
        """
        Create a table with the specified name and columns.
        """
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.execute(query)
        except mysql.connector.Error as err:
            raise  # Rethrow the exception to handle it at a higher level

    def drop_table(self, table_name):
        """
        Drop (delete) a table from the database.
        """
        try:
            query = f"DROP TABLE IF EXISTS {table_name}"
            self.execute(query)
        except mysql.connector.Error as err:
            raise  # Rethrow the exception to handle it at a higher level

    def insert_data(self, table_name, columns, values):
        """
        Insert data into a table.
        """
        try:
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
            self.cursor.execute(query, values)
            self.mydb.commit()
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level

    def update_data(self, table_name, set_values, where_clause):
        """
        Update data in a table based on a WHERE clause.
        """
        try:
            query = f"UPDATE {table_name} SET {set_values} WHERE {where_clause}"
            self.execute(query)
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level

    def delete_data(self, table_name, where_clause):
        """
        Delete data from a table based on a WHERE clause.
        """
        try:
            query = f"DELETE FROM {table_name} WHERE {where_clause}"
            self.execute(query)
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level

    def get_column_names(self, table_name):
        """
        Get the column names of a table.
        """
        try:
            self.cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            return [column[0] for column in self.cursor.fetchall()]
        except mysql.connector.Error as err:
            raise  # Rethrow the exception to handle it at a higher level

    def count_rows(self, table_name):
        """
        Count the number of rows in a table.
        """
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            return self.cursor.fetchone()[0]
        except mysql.connector.Error as err:
            raise  # Rethrow the exception to handle it at a higher level

    def execute_script(self, script):
        """
        Execute a SQL script from a file.
        """
        try:
            with open(script, "r") as sql_file:
                queries = sql_file.read().split(";")
                for query in queries:
                    if query.strip():
                        self.execute(query)
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level

    def create_index(self, table_name, index_name, columns):
        """
        Create an index on specified columns of a table.
        """
        try:
            query = f"CREATE INDEX {index_name} ON {table_name} ({', '.join(columns)})"
            self.execute(query)
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level

    def create_unique_index(self, table_name, index_name, columns):
        """
        Create a unique index on specified columns of a table.
        """
        try:
            query = f"CREATE UNIQUE INDEX {index_name} ON {table_name} ({', '.join(columns)})"
            self.execute(query)
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise  # Rethrow the exception to handle it at a higher level
    
    def add_column(self, table_name, column_name, column_type):
        """
        Add a column to a table.
        """
        try:
            query = f"ALTER TABLE {table_name} ADD {column_name} {column_type}"
            self.execute(query)
        except mysql.connector.Error as err:
            self.mydb.rollback()
            raise
