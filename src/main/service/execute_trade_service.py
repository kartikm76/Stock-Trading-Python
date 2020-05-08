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
            
## work to be done
## 1. insert (B) or update (B) or delete (S) record in stock_holding
## 2. update account_balance
## 3. insert a record in trade_activity