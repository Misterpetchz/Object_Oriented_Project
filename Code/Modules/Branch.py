class Branch():
    def __init__(self, branch_name, open_time, location, tel, line_id, facebook_id, product_in_stock):
        self._branch_name = branch_name
        self._open_time = open_time
        self._location = location
        self._tel = tel
        self._line_id = line_id
        self._facebook_id = facebook_id
        self._product_in_stock = product_in_stock

    @property
    def branch_name(self):
        return self._branch_name
    
    @branch_name.setter
    def branch_name(self,a):
        self._branch_name = a
        
    @property
    def open_time(self):
        return self._open_time
    
    @open_time.setter
    def open_time(self,a):
        self._open_time = a
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self,a):
        self._location = a
        
    @property
    def tel(self):
        return self._tel
    
    @tel.setter
    def tel(self,a):
        self._tel = a
        
    @property
    def line_id(self):
        return self._line_id
    
    @line_id.setter
    def line_id(self,a):
        self._line_id = a
        
    @property
    def facebook_id(self):
        return self._facebook_id
    
    @facebook_id.setter
    def facebook_id(self,a):
        self._facebook_id = a
        
    @property
    def product_in_stock(self):
        return self._product_in_stock
    
    @product_in_stock.setter
    def product_in_stock(self,a):
        self._product_in_stock = a
    

