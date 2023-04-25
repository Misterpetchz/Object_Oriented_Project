from Modules.Catalog import *
class Basket:
    def __init__(self):
        self.__book_item = []
        self.__price = 0
        
    def reduce_amount(self,book):
        for item in self.__book_item:
            if book == item.name:
                item.amount = item.amount-1
                self.__price -= item.price
                if item.amount == 0:
                    self.__book_item.remove(item)
                    
    def add_amount(self,book):
        for item in self.__book_item:
            if book == item.name:
                item.amount = item.amount+1
                self.__price += item.price
                    
    def add_book(self, book):
        self.__book_item.append(book)
    def remove_book(self, index):
        self.__book_item.pop(index)
    def get_book(self):
        return self.__book_item
    def set_book(self, book):
        self.__book_item = book
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

    
    price = property(get_price, set_price)
    book_item = property(get_book, set_book)
