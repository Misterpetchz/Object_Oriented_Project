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
        
    def search_book(search_string):
        pass
    def search_available_branch():
        pass
    def request_edit():
        pass
    def info_verification(email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
        pass
    def modify_credit_card_info(card_num,exp_date,cvc):
        pass
    def add_credit_card_info(card_info):
        pass
    def add_book_to_basket():
        pass
    def make_order(Basket, Coupon):
        pass
    def make_payment(payment_type):
        pass
    
    
class Admin(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, shipping, permission):
        super().__init__(email, password, full_name, gender, tel, shipping)
        self.__permission = permission
        
    def modify_delete_branch(type,Branch):
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
    def add_book(book):
        pass
    def add_event(event_name, event_start, event_end, discounted_book, discounted_price, book_item):
        pass