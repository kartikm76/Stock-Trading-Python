from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.account_balance import AccountBalance
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary
      
class AccountBalanceService:
    def get_account_balance(self, id=None):
        self.id = id
        
        data_rows = None
        account_balance_dictionary = {}
        account_balance_list = []

        with DatabaseConnect() as cursor:
            if self.id is None:
                sql_select_query = "select * from account_balance"
                cursor.execute(sql_select_query)
            else:
                sql_select_query = """select * from account_balance where account_id = %s"""
                cursor.execute(sql_select_query, (self.id,))
            
            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                account_balance_object = AccountBalance()
                account_balance_object.account_id = each_record[0]                
                account_balance_object.balance_amount = SerializeObject.serialize_object(each_record[1])
                account_balance_object.as_of_date = SerializeObject.serialize_object(each_record[2])                
                account_balance_dictionary = ConvertToDictionary.convert_to_dictionary(account_balance_object)
                account_balance_list.append(account_balance_dictionary)
            return account_balance_list