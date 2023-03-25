from Modules.Catalog import *
class Basket:
    def __init__(self, book_item):
        self.__book_item = book_item
        
    def get_book(self, catalog:Catalog, book):
        self.__index = catalog.list_of_book.index(book)
        return catalog.list_of_book.pop(self.__index)
    def add_book(self, catalog, book):
        self.__book_item.append(self.get_book(catalog,book))
    def get_books(self):
        return self.__book_item
    
    book_item = property(get_books)
