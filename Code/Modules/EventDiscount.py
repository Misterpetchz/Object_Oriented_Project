from Modules.Book import Book
from datetime import datetime
import datetime
class EventDiscount():
    def __init__(self, event_name, event_start, event_end, discounted_percentage):
        self.__event_name = event_name
        self.__event_start = event_start
        self.__event_end = event_end
        self.__discounted_percentage = discounted_percentage
        self.__list_of_book = []
        
    def get_event_name(self):
        return self.__event_name
    def get_event_start(self):
        return self.__event_start
    def get_event_end(self):
        return self.__event_end
    def get_event_percentage(self):
        return self.__event_start
    def get_list_of_book(self):
        return self.__list_of_book
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
            if i._name in [x._name for x in self.list_of_book]:
                self.apply_discount(i)
    def apply_discount(self, book):
        book._new_price = book._price * self.__discounted_percentage

    event_name = property(get_event_name)
    event_start = property(get_event_start)
    event_end = property(get_event_end)
    discounted_percentage = property(get_event_percentage)
    list_of_book = property(get_list_of_book)