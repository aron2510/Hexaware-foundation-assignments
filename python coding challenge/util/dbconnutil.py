import pyodbc
from util.dbpropertyutil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        props = {}
        with open('db.properties', 'r') as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    props[key] = value

        conn_str = (
            f"DRIVER={{{props['DB_DRIVER']}}};"
            f"SERVER={props['DB_SERVER']};"
            f"DATABASE={props['DB_NAME']};"
            f"Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        return conn
