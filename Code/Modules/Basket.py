from Modules.Catalog import *
class Basket:
    def __init__(self):
        self.__book_item = []
        self.__price = 0
        
    def add_book(self, book):
        self.__book_item.append(book)
    def remove_book(self, book):
        self.__book_item.pop(1)
    def get_book(self):
        return self.__book_item
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

    
    price = property(get_price, set_price)
    book_item = property(get_book)
