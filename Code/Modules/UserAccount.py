from Modules.Basket import Basket
from Modules.Catalog import Catalog
from Modules.Book import BookItem
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.Rating import Rating
from Modules.EventDiscount import EventDiscount
from Modules.CreditCard import CreditCard

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
    def modify_credit_card_info(self, credit_card:CreditCard, new_card_num, new_expire_date, new_cvc):
        if isinstance(new_card_num, str):
            credit_card.card_num = new_card_num
        if isinstance(new_expire_date, str):
            credit_card.expire_date = new_expire_date
        if isinstance(new_cvc, str):
            credit_card.cvc = new_cvc
    def add_credit_card_info(card_info):
        pass
    def add_book_to_basket(self, catalog,  book):
        self.__basket.add_book(catalog, book)
    def add_rating(self, book:BookItem, rating:Rating):
        book._rating.append(rating)
    def make_order(Basket, Coupon):
        pass
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
    def modify_branch(self, branch:Branch, new_branch_name, new_open_time, new_location, new_tel, new_line_id, new_facebook_id, new_product_in_stock):
        if isinstance(new_branch_name, str):
            branch._branch_name = new_branch_name
        if isinstance(new_open_time, str):
            branch._open_time = new_open_time
        if isinstance(new_location, str):
            branch._location = new_location
        if isinstance(new_tel, str):
            branch._tel = new_tel
        if isinstance(new_line_id, str):
            branch._line_id = new_line_id
        if isinstance(new_facebook_id, str):
            branch._facebook_id = new_facebook_id
        
    def modify_delete_book(type,Book):
        pass
    def modify_book( product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price, event_discount):
        pass
    def modify_delete_event(type,event_name):
        pass
    def apply_event_modification(event_name, event_start, event_end, discounted_book, discounted_price, book_item):
        pass
    def add_book(self, book,catalog:Catalog):
        if book == BookItem:
            catalog.list_of_book.append(book)
    def add_event(self, book:BookItem, event_discount:EventDiscount):
        if isinstance(event_discount, EventDiscount):
            book.event_discount.append(event_discount)