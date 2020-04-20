from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.user_account import UserAccount
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary

class UserAccountService:
    def get_user_account(self, type, id):
        self.type = type
        self.id = id

        data_rows = None
        user_account_dictionary = {}
        user_account_list = []

        with DatabaseConnect() as cursor:
            if self.type == 'USER':
                sql_select_query = """select * from user_account where user_id = %s"""
                
            if self.type == 'ACCOUNT':
                sql_select_query = """select * from user_account where account_id = %s"""        

            cursor.execute(sql_select_query, (self.id,))          
            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                user_account_object = UserAccount()
                user_account_object.user_id = each_record[0]                
                user_account_object.account_id = each_record[1]
                user_account_dictionary = ConvertToDictionary.convert_to_dictionary(user_account_object)
                user_account_list.append(user_account_dictionary)
            return user_account_list