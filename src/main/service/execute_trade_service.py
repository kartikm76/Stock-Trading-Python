from mysql.connector import Error
from utils.db_connect import DatabaseConnect
from flask import Flask, request
from model.trade import Trade

class ExecuteTradeService:
    def __init__(self):        
        self.tradeObject = Trade()       

    def manage_stock_holding(self, data):
        self.tradeObject = data        
        print (self.tradeObject)
        return self.tradeObject
