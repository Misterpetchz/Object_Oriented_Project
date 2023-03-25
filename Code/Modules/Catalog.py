class Catalog():
    def __init__(self, list_of_book):
        self.__list_of_book = list_of_book

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
    def add_book(book):
        pass
    def get_list(self):
        return self.__list_of_book
    def set_list(self, new_list):
        self.__list_of_book = new_list
    
    list_of_book = property(get_list, set_list)