from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.stock import Stock
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary

class StockService:
    def get_stock_details(self, id=None):        
        self.id = id

        data_rows = None
        stock_dictionary = {}
        stock_list = []

        with DatabaseConnect() as cursor:
            if self.id is None:
                sql_select_query = """select stock_symbol, stock_name, last_price from stock_master"""
                cursor.execute(sql_select_query)
            else:
                sql_select_query = """select stock_symbol, stock_name, last_price from stock_master where stock_symbol = %s"""
                cursor.execute(sql_select_query, (self.id,))
                            
            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                stock_object = Stock()
                stock_object.stock_symbol = each_record[0]
                stock_object.stock_name = each_record[1]                
                stock_object.last_price = SerializeObject.serialize_object(each_record[2])

                stock_dictionary = ConvertToDictionary.convert_to_dictionary(stock_object)
                stock_list.append(stock_dictionary)
            return stock_list