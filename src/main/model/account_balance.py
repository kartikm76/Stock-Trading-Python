class AccountBalance:    
    ## account_id
    @property
    def account_id (self):
        return self._account_id
        
    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id
    
    ## balance_amount
    @property
    def balance_amount (self):
        return self._balance_amount
        
    @balance_amount.setter
    def balance_amount(self, balance_amount):
        self._balance_amount = balance_amount

    ## as_of_date
    @property
    def as_of_date (self):
        return self._as_of_date
        
    @as_of_date.setter
    def as_of_date(self, as_of_date):
        self._as_of_date = as_of_date