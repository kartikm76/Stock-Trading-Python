from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.account import Account
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary
      
class AccountService:
    def get_account_details(self, id=None):
        self.id = id
        
        data_rows = None
        account_dictionary = {}
        accounts_list = []

        with DatabaseConnect() as cursor:
            if self.id is None:
                sql_select_query = "select * from account_master"
                cursor.execute(sql_select_query)
            else:
                sql_select_query = """select * from account_master where id = %s"""
                cursor.execute(sql_select_query, (self.id,))
                      
            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                account_object = Account()
                account_object.id = each_record[0]                
                account_object.type = each_record[1]
                account_object.open_date = SerializeObject.serialize_object(each_record[2])
                account_object.isActive = each_record[3]                
                account_dictionary = ConvertToDictionary.convert_to_dictionary(account_object)
                accounts_list.append(account_dictionary)
            return accounts_list