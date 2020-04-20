class TradeActivity:
    
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
    
    ## transaction_qty
    @property
    def transaction_qty (self):
        return self._transaction_qty
        
    @transaction_qty.setter
    def transaction_qty(self, transaction_qty):
        self._transaction_qty = transaction_qty
    
    ## transaction_price
    @property
    def transaction_price (self):
        return self._transaction_price
        
    @transaction_price.setter
    def transaction_price(self, transaction_price):
        self._transaction_price = transaction_price

    ## transaction_type_code
    @property
    def transaction_type_code (self):
        return self._transaction_type_code
        
    @transaction_type_code.setter
    def transaction_type_code(self, transaction_type_code):
        self._transaction_type_code = transaction_type_code
    
    ## transaction_date
    @property
    def transaction_date (self):
        return self._transaction_date
        
    @transaction_date.setter
    def transaction_date(self, transaction_date):
        self._transaction_date = transaction_date