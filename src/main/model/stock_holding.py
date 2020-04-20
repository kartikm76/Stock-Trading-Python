class StockHolding:    
    ## user_id
    @property
    def user_id (self):
        return self._user_id
        
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    ## account_id
    @property
    def account_id (self):
        return self._account_id
        
    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    ## stock_symbol
    @property
    def stock_symbol (self):
        return self._stock_symbol
        
    @stock_symbol.setter
    def stock_symbol(self, stock_symbol):
        self._stock_symbol = stock_symbol
    
    ## holding_qty
    @property
    def holding_qty (self):
        return self._holding_qty
        
    @holding_qty.setter
    def holding_qty(self, holding_qty):
        self._holding_qty = holding_qty
    
    ## purchase_price
    @property
    def purchase_price (self):
        return self._purchase_price
        
    @purchase_price.setter
    def purchase_price(self, purchase_price):
        self._purchase_price = purchase_price