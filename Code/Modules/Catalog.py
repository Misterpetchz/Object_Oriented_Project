from Modules.Book import BookItem
class Catalog():
    def __init__(self, list_of_book):
        self.__all_list_of_book = list_of_book

    def get_book_info(search_string):
        pass
    def remove_book(book):
        pass
    def modify_book(book):
        pass
    def find_book(Book):
        pass
    def add_to_basket(Book):
        pass
    def add_book(self, book):
        if isinstance(book, BookItem):
            self.__all_list_of_book.append(book)
    def search_book(self, search_string):
        self.__list_of_book = []
        for element in self.__all_list_of_book:
            if search_string in element._name:
                self.__list_of_book.append(element)
        self.__list_of_book
    def get_all_list(self):
        return self.__all_list_of_book
    def set_all_list(self, new_list):
        self.__all_list_of_book = new_list
    def get_list(self):
        return self.__list_of_book
    
    list_all_of_book = property(get_all_list, set_all_list)
    list_of_book = property(get_list)