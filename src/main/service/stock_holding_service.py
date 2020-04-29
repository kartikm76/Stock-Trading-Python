from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.stock_holding import StockHolding
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary

class StockHoldingService:
    def get_stock_holding(self, type=None, id=None):  
        self.type = type
        self.id = id

        data_rows = None
        stock_holding_dictionary = {}
        stock_holding_list = []

        with DatabaseConnect() as cursor:
            if self.id is None:
                sql_select_query = """  select a.user_id, b.account_id, b.stock_symbol, b.holding_qty, b.purchase_price 
                                        from user_account a, stock_holding b 
                                        where a.account_id = b.account_id """
                cursor.execute(sql_select_query)
            else:
                if self.type == 'USER':
                    sql_select_query = """  select a.user_id, b.account_id, b.stock_symbol, b.holding_qty, b.purchase_price 
                                            from user_account a, stock_holding b 
                                            where a.account_id = b.account_id and a.user_id = %s"""
                    
                if self.type == 'ACCOUNT':
                    sql_select_query = """  select a.user_id, b.account_id, b.stock_symbol, b.holding_qty, b.purchase_price 
                                            from user_account a, stock_holding b 
                                            where a.account_id = b.account_id and a.account_id = %s"""
                
                cursor.execute(sql_select_query, (self.id,))

            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                stock_holding_object = StockHolding()
                stock_holding_object.user_id = each_record[0]                
                stock_holding_object.account_id = each_record[1]
                stock_holding_object.stock_symbol = each_record[2]
                stock_holding_object.holding_qty = each_record[3]                
                stock_holding_object.purchase_price = SerializeObject.serialize_object(each_record[4])

                stock_holding_dictionary = ConvertToDictionary.convert_to_dictionary(stock_holding_object)
                stock_holding_list.append(stock_holding_dictionary)
            return stock_holding_list