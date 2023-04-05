from Modules.Basket import Basket
from Modules.Catalog import Catalog
from Modules.Book import *
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
        self.__basket = Basket()
        self.__order_id = 1
        self.__order_list = []
    def request_edit():
        pass
    def info_verification(email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
        pass
    def modify_credit_card_info(card_num,exp_date,cvc):
        pass
    def add_credit_card_info(card_info):
        pass
    def add_book_to_basket(self, book_item, book:Book):
        self.__basket.add_book(book_item)
        book._amount_in_stock -= 1
        self.__basket.price += book_item._price
    def remove_book_from_basket(self, book_item, book:Book):
        self.__basket.remove_book(book_item)
        book._amount_in_stock += 1
        self.__basket.price -= book_item._price
    def make_order(self, order):
        if len(self.__basket.book_item) > 0:
            self.__order_list.append(order)
            self.__order_id+=1
    def make_payment(payment_type):
        pass
    def get_basket(self):
        return self.__basket
    def get_order_list(self):
        return self.__order_list
    def get_order_id(self):
        return self.__order_id
    order_list = property(get_order_list)
    basket = property(get_basket)
    order_id = property(get_order_id)
    
    
class Admin(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, shipping, permission):
        super().__init__(email, password, full_name, gender, tel, shipping)
        self.__permission = permission
        
    def modify_delete_branch(type,Branch):
        pass
        
    def add_branch(self, branch_list:BranchList, branch:Branch):
            branch_list.list_of_branch.append(branch)
            
    def modify_branch(branch_name, open_time, location, tel, line_id, facebook_id, gps, product_in_stock):
        pass
    
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
        if isinstance(book, BookItem):
            catalog.list_of_book.append(book)
    def add_event(event_name, event_start, event_end, discounted_book, discounted_price, book_item):
        pass