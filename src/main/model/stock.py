class Stock:
    ## stock_symbol
    @property
    def stock_symbol (self):
        return self._stock_symbol
        
    @stock_symbol.setter
    def stock_symbol(self, stock_symbol):
        self._stock_symbol = stock_symbol
    
    ## stock_name
    @property
    def stock_name (self):
        return self._stock_name
        
    @stock_name.setter
    def stock_name(self, stock_name):
        self._stock_name = stock_name
    
    ## last_price
    @property
    def last_price (self):
        return self._last_price
        
    @last_price.setter
    def last_price(self, last_price):
        self._last_price = last_price