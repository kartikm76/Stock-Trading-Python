from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.trade_activity import TradeActivity
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary

class TradeActivityService:
    def get_trade_activity(self, id=None):        
        self.id = id

        data_rows = None
        trade_activity_dictionary = {}
        trade_activity_list = []

        with DatabaseConnect() as cursor:
            if self.id is None:
                sql_select_query = """  select a.account_id, a.stock_symbol, a.transaction_qty, a.transaction_price, b.description as transaction_type, 
                                        a.transaction_date from trade_activity a, transaction_type_code b 
                                        where a.transaction_type_code = b.code order by a.account_id"""
                cursor.execute(sql_select_query)
            else:
                sql_select_query = """  select a.account_id, a.stock_symbol, a.transaction_qty, a.transaction_price, b.description as transaction_type, 
                                        a.transaction_date from trade_activity a, transaction_type_code b 
                                        where a.transaction_type_code = b.code 
                                        and account_id = %s"""
                cursor.execute(sql_select_query, (self.id,))

            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                trade_activity_object = TradeActivity()
                trade_activity_object.account_id = each_record[0]                
                trade_activity_object.stock_symbol = each_record[1]
                trade_activity_object.transaction_qty = each_record[2]
                trade_activity_object.transaction_price = SerializeObject.serialize_object(each_record[3])
                trade_activity_object.transaction_type_code = each_record[4]
                trade_activity_object.transaction_date = SerializeObject.serialize_object(each_record[5])

                trade_activity_dictionary = ConvertToDictionary.convert_to_dictionary(trade_activity_object)
                trade_activity_list.append(trade_activity_dictionary)
            return trade_activity_list