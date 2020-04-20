from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from flask import Flask, request

class ExecuteTradeService:
    def manage_stock_holding(self, params):
        print ("coming here")
        print (params)
