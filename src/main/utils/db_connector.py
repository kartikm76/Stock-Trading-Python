import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connection_config_dict = {
                'user': 'root',
                'password': 'password',
                'host': 'localhost',
                'database': 'stock-trading',
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 5,
                'pool_name': "stock-trading-connection_pool",
                'pool_reset_session': True
            }
           
    def get_connection(self):        
        try:            
            connection_pool = mysql.connector.pooling.MySQLConnectionPool(**self.connection_config_dict)

            print ("Printing connection pool properties ")
            print("Connection Pool Name - ", connection_pool.pool_name)
            print("Connection Pool Size - ", connection_pool.pool_size)

            # Get connection object from a pool
            self.connection = connection_pool.get_connection()


            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
                self.cursor = self.connection.cursor()                
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print ("Your connected to - ", record)
                return self.cursor

        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
        # finally:
        #     #closing database connection.
        #     if(self.connection.is_connected()):
        #         self.cursor.close()
        #         self.connection.close()
        #         print("MySQL connection is closed")


        # def __enter__(self):
        #     self.connection = Database.get_connection()
        #     self.cursor = self.connection.cursor()
        #     return self.cursor

        # def __exit__(self, exception_type, exception_value, exception_traceback):
        #     if exception_value is not None:
        #         self.connection.rollback()
        #     else:
        #         self.cursor.close()
        #         self.connection.commit()
        #     Database.return_connection(self.connection)


            #connection = mysql.connector.connect(**connection_config_dict)
        #     if connection.is_connected():
        #         db_Info = connection.get_server_info()
        #         print("Connected to MySQL Server version ", db_Info)
        #         cursor = connection.cursor()

        #         #global conneection timeout arguments
        #         global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        #         global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        #         global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        #         cursor.execute("select database();")
        #         record = cursor.fetchone()
        #         print("You're connected to database: ", record)

        # except Error as e:
        #     print("Error while connecting to MySQL", e)
        # finally:
        #     if (connection.is_connected()):
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")