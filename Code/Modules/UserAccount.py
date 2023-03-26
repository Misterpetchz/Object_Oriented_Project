from Modules.Basket import Basket
from Modules.Catalog import Catalog
from Modules.Book import BookItem
from Modules.Branch import Branch
from Modules.BranchList import BranchList

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
    def modify_credit_card_info(card_num,exp_date,cvc):
        pass
    def add_credit_card_info(card_info):
        pass
    def add_book_to_basket(self, catalog,  book):
        self.__basket.add_book(catalog, book)
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
        
    def modify_delete_branch(self,type,branch_list:BranchList,Branch):
        if type == "modify":
            self.selected_branch = branch_list.get_specific_branch(Branch)
            self.new_name = input("Enter new name : ")
            self.new_time = input("Enter new time : ")
            self.new_location = input("Enter new location : ")
            self.new_tel = input("Enter new tel : ")
            self.new_line_id = input("Enter new line id : ")
            self.new_facebook_id = input("Enter new facebook id : ")
            self.new_product_in_stock = input("Enter new product in stock : ").split(" ")
            modified = self.modify_branch(branch_list,self.selected_branch,self.new_name, self.new_time, self.new_location,self.new_tel,self.new_line_id,self.new_facebook_id,self.new_product_in_stock)
        elif type == "delete":
            self.selected_branch = branch_list.remove_branch(Branch)
        
    def add_branch(self, branch_list:BranchList, branch):
        if isinstance(branch, Branch):
            branch_list.list_of_branch.append(branch)
            
    def modify_branch(self,branch_list:BranchList,branch:Branch,new_name, new_time, new_location, new_tel, new_line_id, new_facebook_id, new_product_in_stock):
        if new_name != "":
            branch.branch_name = new_name
        if new_location != None:
            branch.location = new_location
        if new_time != None:
            branch.open_time = new_time
        if new_tel != None:
            branch.tel = new_tel
        if new_line_id != None:
            branch.line_id = new_line_id
        if new_facebook_id != None:
            branch.facebook_id = new_facebook_id
        if new_product_in_stock != None:
            branch.product_in_stock = new_product_in_stock
        return branch
            
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