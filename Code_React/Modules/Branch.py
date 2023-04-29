from Modules.Book import Book

class Branch():
    def __init__(self, branch_name, open_time, location, tel, line_id, facebook_id):
        self._branch_name = branch_name
        self._open_time = open_time
        self._location = location
        self._tel = tel
        self._line_id = line_id
        self._facebook_id = facebook_id
        self._product_in_stock = []
        
    def add_product(self, book):
        self._product_in_stock.append(book)

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
        

    def modify_branch(self, new_branch_name, new_open_time, new_location, new_tel, new_line_id, new_facebook_id, list_add_book, list_delete_book):
        if isinstance(new_branch_name, str):
            if new_branch_name != '':
                self._branch_name = new_branch_name
        if isinstance(new_open_time, str):
            if new_open_time != '':
                self._open_time = new_open_time
        if isinstance(new_location, str):
            if new_location != '':
                self._location = new_location
        if isinstance(new_tel, str):
            if new_tel != '':
                self._tel = new_tel
        if isinstance(new_line_id, str):
            if new_line_id != '':
                self._line_id = new_line_id
        if isinstance(new_facebook_id, str):
            if new_facebook_id != '':
                self._facebook_id = new_facebook_id
        if isinstance(list_add_book, list):
            for book in list_add_book:
                if book not in self._product_in_stock:
                    self._product_in_stock.append(book)
        if isinstance(list_delete_book, list):
            for book in list_delete_book:
                self._product_in_stock.remove(book)
    
    def add_book_to_stock(self, book:Book):
        if book not in self._product_in_stock:
            self._product_in_stock.append(book)