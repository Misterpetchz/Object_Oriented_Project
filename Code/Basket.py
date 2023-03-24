from Catalog import *
class Basket:
    def __init__(self, book_item):
        self._book_item = book_item
        
    def get_book(self, catalog, book):
        self.index = catalog._list_of_book.index(book)
        return catalog._list_of_book.pop(self.index)
    def add_book(self, catalog, book):
        self._book_item.append(self.get_book(catalog,book))    