from Modules.Book import Book
from datetime import datetime
import math
import datetime
class EventDiscount():
    def __init__(self, event_name, event_start, event_end, discounted_percentage, event_genre):
        self.__event_name = event_name
        self.__event_start = event_start
        self.__event_end = event_end
        self.__discounted_percentage = discounted_percentage
        self.__event_genre = event_genre
        
    ################################################################################################################## 
        #GETTER/SETTER#
    @property   
    def event_name(self):
        return self.__event_name
    @property
    def event_start(self):
        return self.__event_start
    @property
    def event_end(self):
        return self.__event_end
    @property
    def discounted_percentage(self):
        return self.__event_start
    @property
    def list_of_book(self):
        return self.__list_of_book
    #################################################################################################################
    def add_book_to_event(self, book:Book):
        self.__list_of_book.append(book)
    def modify_event(self, new_name, new_start, new_end, new_percentage):
        if isinstance(new_name, str):
            self.__event_name = new_name
        if isinstance(new_start, str):
            self.__event_start = new_start
        if isinstance(new_end, str):
            self.__event_end = new_end
        if isinstance(new_percentage, float):
            self.__discounted_percentage = new_percentage
    def remove_book(self, book:Book):
        for i in self.__list_of_book:
            if i == book:
                self.__list_of_book.remove(book)
                
    def event_dis(self, catalog):
        for i in catalog.list_all_of_book:
            if self.__event_genre in i._genre:
                self.apply_discount(i)

    def apply_discount(self, book):
        book._new_price = math.floor(book._price * self.__discounted_percentage)
