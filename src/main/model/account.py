class Account:

    ## id
    @property
    def id (self):
        return self._id
        
    @id.setter
    def id(self, id):
        self._id = id

    ## type
    @property
    def type (self):
        return self._type
        
    @type.setter
    def type(self, type):
        self._type = type
    
    ## open_date
    @property
    def open_date (self):
        return self._open_date
        
    @open_date.setter
    def open_date(self, open_date):
        self._open_date = open_date
    
    ## isActive
    @property
    def isActive (self):
        return self._isActive
        
    @isActive.setter
    def isActive(self, isActive):
        self._isActive = isActive
