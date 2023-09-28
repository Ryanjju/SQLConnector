from connector import DatabaseConnector

db = DatabaseConnector("localhost", "root", "", "test")
db.connect()


table_name = "test_table"
columns = ["id INT AUTO_INCREMENT PRIMARY KEY", "name VARCHAR(255) NOT NULL"]
db.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")

columns = ["name"]
values = ["John"]
db.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ('{values[0]}')")

db.drop_table(table_name)

db.close()
