from Modules.Catalog import *
class Basket:
    def __init__(self, book_item):
        self.__book_item = book_item
        
    def add_book(self, book):
        self.__book_item.append(book)
    def get_books(self):
        return self.__book_item
    
    book_item = property(get_books)
