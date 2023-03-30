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
    def calculate_price(self, event):
        self.__price = 0
        for book_element in self.__book_item:
            for book_event in event.list_of_book:
                if  book_element._name==book_event._name:
                    self.__price += book_element._price * event.discounted_percentage

    
    price = property(get_price)
    book_item = property(get_book)
