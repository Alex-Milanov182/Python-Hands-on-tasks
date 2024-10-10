import pandas as pd
import json
import sqlite3  # For the DatabaseReader
from abc import ABC, abstractmethod

class Reader(ABC):
    @abstractmethod
    def read(self):
        pass



class CSVReader(Reader):
    def __init__(self, file_path):
        self.file_path = file_path

    
    def read(self):
        return pd.read_csv(file_path)



class JSONReader(Reader):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return pd.json_normalize(data)


class DatabaseReader(Reader):
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name

    def read(self):
        conn = sqlite3.connect(self.db_path)
        query = f"SELECT * FROM {self.table_name}"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df


# Reader Factory Class
class ReaderFactory:
    @staticmethod
    def get_reader(reader_type: str, *args):
        if reader_type == 'csv':
            return CSVReader(*args)
        elif reader_type == 'json':
            return JSONReader(*args)
        elif reader_type == 'db':
            return DatabaseReader(*args)
        else:
            raise ValueError(f"Unknown reader type: {reader_type}")



if __name__ == "__main__":
    # Example usage of ReaderFactory to read a CSV file
    csv_reader = ReaderFactory.get_reader('csv', 'data.csv')
    csv_data = csv_reader.read()
    print("CSV Data:")
    print(csv_data)

    # Example usage of ReaderFactory to read a JSON file
    json_reader = ReaderFactory.get_reader('json', 'data.json')
    json_data = json_reader.read()
    print("\nJSON Data:")
    print(json_data)

    # Example usage of ReaderFactory to read from a database
    db_reader = ReaderFactory.get_reader('db', 'database.db', 'table_name')
    db_data = db_reader.read()
    print("\nDatabase Data:")
    print(db_data)