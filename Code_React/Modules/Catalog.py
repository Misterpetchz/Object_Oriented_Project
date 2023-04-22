from Modules.Book import Book
from Modules.EventDiscount import EventDiscount
class Catalog():
    def __init__(self):
        self.__all_list_of_book = []

    def get_book_info(search_string):
        pass
    def remove_book(book):
        pass
    def find_book(Book):
        pass
    def add_to_basket(Book):
        pass
    def add_book(self, book):
        self.__all_list_of_book.append(book)
    def find_book_by_name(self, name):
        for i in self.list_all_of_book:
            if name == i._name:
                return i
    def search_book(self, search_string):
        self.__list_of_book = []
        for element in self.__all_list_of_book:
            if search_string in element._name:
                self.__list_of_book.append(element)
        self.__list_of_book
        
    ##################################################################################################################
        #GETTER/SETTER#
    @property
    def list_all_of_book(self):
        return self.__all_list_of_book
    @list_all_of_book.setter
    def list_all_of_book(self, new_list):
        self.__all_list_of_book = new_list
    @property
    def list_of_book(self):
        return self.__list_of_book
    ##################################################################################################################