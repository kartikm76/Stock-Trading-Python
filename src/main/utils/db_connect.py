import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling

class Database:
    __connection_pool = None
    __connection_count = 0
    __connection_config_dict = {
                'user': 'root',
                'password': 'password',
                'host': 'localhost',
                'database': 'stock-trading',
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 10,
                'pool_name': "stock-trading-connection_pool",
                'pool_reset_session': True
            }
    
    @classmethod
    def initialize_connection_pool(cls):
        cls.__connection_pool = mysql.connector.pooling.MySQLConnectionPool(**cls.__connection_config_dict)        
        
    @classmethod
    def get_connection(cls):
        cls.__connection_count = cls.__connection_count + 1
        print ("New Connection # - " + str(cls.__connection_count))
        return cls.__connection_pool.get_connection()
        
    @classmethod
    def return_connection(cls, connection):
        cls.__connection_count = cls.__connection_count - 1        
        connection.close()
        print ("Returning Connection # - " + str(cls.__connection_count))

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()
        print ("Closing Connection # - " + str(cls.__connection_count))

class DatabaseConnect:
    def __init__(self):
        self.connection = None
        self.cursor = None        

    def __enter__(self):
        self.connection = Database.get_connection()
        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
            self.cursor = self.connection.cursor()
            return self.cursor
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)