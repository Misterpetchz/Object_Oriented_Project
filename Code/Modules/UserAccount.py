from Modules.Basket import Basket
from Modules.Catalog import Catalog
from Modules.Book import BookItem
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.Order import Order

class UserAccount:
    def __init__(self, email, password, full_name, gender, tel , shipping):
        self._email = email
        self._password = password
        self._full_name = full_name
        self._gender = gender
        self._tel = tel
        self._shipping = shipping

# Inheritance from UserAccount

class Customer(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
        super().__init__(email, password, full_name, gender, tel, shipping)
        self._address = address
        self.__email_notification = email_notification
        self.__sms_notification = sms_notification
        self.__basket = Basket([])
        self.__order_id = 1
        self.__order_list = []
    def search_book(self, search_string, catalog:Catalog):
        lists=[]
        for element in catalog.list_of_book:
            if search_string in element._name:
                lists.append(element)
        return lists
    def search_available_branch(self, book, all_branch):
        lists = []
        for element in all_branch.list_of_branch:
            for elements in element._product_in_stock:
                if elements == book:
                    lists.append(element)
        return lists
    def request_edit():
        pass
    def info_verification(email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
        pass
    def modify_credit_card_info(card_num,exp_date,cvc):
        pass
    def add_credit_card_info(card_info):
        pass
    def add_book_to_basket(self, catalog,  book):
        self.__basket.add_book(catalog, book)
    def make_order(self, coupon=0):
        if coupon != 0:
            
        if len(self.__basket.book_item) > 0:
            self.__order_list.append(Order(self.__basket,
                                        self.__order_id,
                                        False,
                                        False,
                                        self
                                        ))
            self.__order_id+=1
    def make_payment(payment_type):
        pass
    def get_basket(self):
        return self.__basket
        
    basket = property(get_basket)
    
    
class Admin(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, shipping, permission):
        super().__init__(email, password, full_name, gender, tel, shipping)
        self.__permission = permission
        
    def modify_delete_branch(type,Branch):
        pass
    def add_branch(self, branch_list:BranchList, branch):
        if isinstance(branch, Branch):
            branch_list.list_of_branch.append(branch)
    def modify_branch(branch_name, open_time, location, tel, line_id, facebook_id, gps, product_in_stock):
        pass
    def modify_delete_book(type,Book):
        pass
    def modify_book( product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price, event_discount):
        pass
    def modify_delete_event(type,event_name):
        pass
    def apply_event_modification(event_name, event_start, event_end, discounted_book, discounted_price, book_item):
        pass
    def add_rating(rating):
        pass
    def add_book(self, book,catalog:Catalog):
        if book == BookItem:
            catalog.list_of_book.append(book)
    def add_event(event_name, event_start, event_end, discounted_book, discounted_price, book_item):
        pass