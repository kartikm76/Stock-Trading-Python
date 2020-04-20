class UserAccount:
    
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
    def account_id(self, _account_id):
        self._account_id = _account_id
