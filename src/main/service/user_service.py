from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from model.user import User
from utils.object_serialize import SerializeObject
from utils.convert_to_dictionary import ConvertToDictionary

class UserService:
    def get_user_details(self, id=None):
        self.id = id
        
        data_rows = None
        user_dictionary = {}
        users_list = []

        with DatabaseConnect() as cursor:
            if self.id is None:
                sql_select_query = "select * from user_master"
                cursor.execute(sql_select_query)
            else:
                sql_select_query = """select * from user_master where id = %s"""
                cursor.execute(sql_select_query, (self.id,))
                      
            data_rows = cursor.fetchall()
            print("Total number of rows: ", cursor.rowcount)
            
            for each_record in data_rows:
                user_object = User()
                user_object.id = each_record[0]                
                user_object.name = each_record[1]
                user_object.ssn = each_record[2]
                user_object.isActive = each_record[3]                
                user_object.profile_create_date = SerializeObject.serialize_object(each_record[4])
                user_dictionary = ConvertToDictionary.convert_to_dictionary(user_object)
                users_list.append(user_dictionary)
            return users_list
