class User:
    
    ## id
    @property
    def id (self):
        return self._id
        
    @id.setter
    def id(self, id):
        self._id = id

    ## name
    @property
    def name (self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
    
    ## ssn
    @property
    def ssn (self):
        return self._ssn
        
    @ssn.setter
    def ssn(self, ssn):
        self._ssn = ssn
    
    ## isActive
    @property
    def isActive (self):
        return self._isActive
        
    @isActive.setter
    def isActive(self, isActive):
        self._isActive = isActive
    

    ## profile_create_date
    @property
    def profile_create_date (self):
        return self._profile_create_date
        
    @profile_create_date.setter
    def profile_create_date(self, profile_create_date):
        self._profile_create_date = profile_create_date