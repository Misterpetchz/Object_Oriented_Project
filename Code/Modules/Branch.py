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


