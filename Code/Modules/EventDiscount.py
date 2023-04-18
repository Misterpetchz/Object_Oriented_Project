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
        
    def get_event_name(self):
        return self.__event_name
    def get_event_start(self):
        return self.__event_start
    def get_event_end(self):
        return self.__event_end
    def get_event_percentage(self):
        return self.__event_start
    
    @property
    def event_genre(self):
        return self.__event_genre
    @event_genre.setter
    def event_genre(self, new_value):
        self.__event_genre = new_value

    def modify_event(self, new_name, new_start, new_end, new_percentage, new_genre):
        if isinstance(new_name, str):
            self.__event_name = new_name
        if isinstance(new_start, str):
            self.__event_start = new_start
        if isinstance(new_end, str):
            self.__event_end = new_end
        if isinstance(new_percentage, int):
            self.__discounted_percentage = new_percentage
        if isinstance(new_genre, str):
            self.__event_genre = new_genre
            
    def event_dis(self, catalog):
        for i in catalog.list_all_of_book:
            if self.__event_genre in i._genre:
                self.apply_discount(i)
    def apply_discount(self, book):
        book._new_price = math.floor(book._price * self.__discounted_percentage)

    event_name = property(get_event_name)
    event_start = property(get_event_start)
    event_end = property(get_event_end)
    discounted_percentage = property(get_event_percentage)