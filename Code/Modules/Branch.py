class Branch():
    def __init__(self, branch_name, open_time, location, tel, line_id, facebook_id, product_in_stock):
        self._branch_name = branch_name
        self._open_time = open_time
        self._location = location
        self._tel = tel
        self._line_id = line_id
        self._facebook_id = facebook_id
        self._product_in_stock = product_in_stock

    def modify_branch(self, new_branch_name, new_open_time, new_location, new_tel, new_line_id, new_facebook_id, list_add_book, list_delete_book):
        if isinstance(new_branch_name, str):
            self._branch_name = new_branch_name
        if isinstance(new_open_time, str):
            self._open_time = new_open_time
        if isinstance(new_location, str):
            self._location = new_location
        if isinstance(new_tel, str):
            self._tel = new_tel
        if isinstance(new_line_id, str):
            self._line_id = new_line_id
        if isinstance(new_facebook_id, str):
            self._facebook_id = new_facebook_id
        if isinstance(list_add_book, list):
            for book in list_add_book:
                if book not in self._product_in_stock:
                    self._product_in_stock.append(book)
        if isinstance(list_delete_book, list):
            for book in list_delete_book:
                self._product_in_stock.remove(book)

