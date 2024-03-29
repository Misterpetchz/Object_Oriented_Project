    # ? Module
from Modules.Basket import Basket
from Modules.Catalog import Catalog
from Modules.Book import *
from Modules.Branch import Branch
from Modules.BranchList import BranchList
from Modules.Order import Order
from Modules.Rating import Rating
from Modules.EventDiscount import EventDiscount
from Modules.CreditCard import CreditCard
from Modules.settings import *
from Modules.Payment import *
import hashlib
import datetime


class UserAccount:
    def __init__(self, email, password, full_name, gender, tel):
        self._email = email
        self._password = password
        self._full_name = full_name
        self._gender = gender
        self._tel = tel

# Inheritance from UserAccount


class Admin(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, permission):
        super().__init__(email, password, full_name, gender, tel)
        self.__permission = permission
        self._disabled = False

    def modify_delete_branch(type, Branch):
        pass

    def add_branch(self, branch_list: BranchList, branch: Branch):
        branch_list.list_of_branch.append(branch)

    def modify_delete_book(type, Book):
        pass

    def modify_book(product_id, cover, brief, creator, name, book_info, book_ISBN_id, book_publisher, book_preview, critic_review, table_of_content, summary, genre, date_created, rating, price, event_discount):
        pass

    def modify_delete_event(type, event_name):
        pass

    def apply_event_modification(event_name, event_start, event_end, discounted_book, discounted_price, book_item):
        pass

    def add_book(self, book, catalog: Catalog):
        if isinstance(book, BookItem):
            catalog.list_of_book.append(book)

    def add_event(self, book: BookItem, event_discount: EventDiscount):
        if isinstance(event_discount, EventDiscount):
            book.event_discount.append(event_discount)


class Customer(UserAccount):
    def __init__(self, email, password, fullname, gender, tel, email_noti, sms_noti, address):
        super().__init__(email, password, fullname, gender, tel)
        self._address = address
        self.__email_notification = email_noti #bool
        self.__sms_notification = sms_noti #bool
        self.__basket = Basket()
        self._disabled = False
        self.__order_list = []
        self.__credit_card = None
        self.__order_id = 1
        self.__order = None
        self.__payment = None
        self.__payment_id = None

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

    def modify_credit_card_info(card_num,exp_date,cvc):
        pass
    def info_verification(email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
        pass
    def add_credit_card(self, credit_card):
        self.__credit_card = credit_card
        
    @property
    def credit_card(self):
        return self.__credit_card
    
    def add_book_to_basket(self, book_item, book:Book):
        if book._amount_in_stock > 0:
            for i in self.__basket.get_book():
                if i.name.lower() == book_item.name.lower():
                    i.amount = i.amount + 1
                    book._amount_in_stock -= 1
                    self.__basket.price += book_item._price
            else:
                self.__basket.add_book(book_item)
                book._amount_in_stock -= 1
                self.__basket.price += book_item._price
        
    def reduce_amount(self,book_item,book:Book):
        for item in self.basket.book_item:
            if book_item == item.name:
                item.amount = item.amount-1
                book._amount_in_stock +=1
                self.basket.price -= item.price
                if item.amount == 0:
                    self.basket.book_item.remove(item)
                    
    def add_amount(self,book_item,book:Book):
        if book._amount_in_stock > 0:
            for item in self.basket.book_item:
                if book_item == item.name:
                    item.amount = item.amount+1
                    book._amount_in_stock -=1
                    self.basket.price += item.price
    def generate_seed(self, payment_id:str):
        payment_id = hashlib.sha256(payment_id.encode())    
        self.__payment_id = payment_id.hexdigest()

    def make_order(self, order):
        if len(self.__basket.book_item) > 0 and self.__payment == None:
            # self.__order_list.append(order)
            # self.__order_id += 1
            self.__order = order
            self.generate_seed(self._email + str(self.__order_id))

    def make_payment(self, payment_type):
        current_date = datetime.date.today()
        format_date = current_date.strftime('%d-%m-%Y') 
        if payment_type.lower() == 'qrcode':
            self.__payment = ViaQrCode(self.__basket.price, format_date)
            return self.__payment.generate_qr_code()
        
        elif payment_type.lower() == 'creditcard':
            self.__payment = ViaCreditCard(self.__basket.price, format_date)
            # if self.__credit_card == None:
            #     return {'credit_card' : None}
            # elif self.__credit_card:
            #     return {'credit_card' : self.__payment}
        
    def add_order_to_order_list(self, order):
        self.__order_list.append(order)
    
    def update_order_id(self):
        self.__order_id += 1

    def reset_payment(self):
        self.__payment = None
        self.__payment_id = None
        self.__order = None

    def get_basket(self):
        return self.__basket
    def get_order_list(self):
        return self.__order_list
    def get_order_id(self):
        return self.__order_id
    def get_email_noti(self):
        return self.__email_notification
    def get_sms_noti(self):
        return self.__sms_notification
    def set_email_noti(self, value):
        self.__email_notification = value
    def set_sms_noti(self, value):
         self.__sms_notification = value

    @property     
    def payment_id(self):
        return self.__payment_id
    
    @property
    def order(self):
        return self.__order
    
    @property
    def payment(self):
        return self.__payment

    order_list = property(get_order_list)
    basket = property(get_basket)
    order_id = property(get_order_id)

    email_notification = property(get_email_noti, set_email_noti)
    sms_notification = property(get_sms_noti, set_sms_noti)
    def toJSON(self) :
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        pass
    #! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # def verify_password(plain_password, hashed_password) :
    #     return PWD_CONTEXT.verify(plain_password, hashed_password)

    # def get_password_hash(password) :
    #     return PWD_CONTEXT.hash(password)

    # def get_user(username : str) :
    #     user = InstanceFinder(Customer, "_email", username)
    #     if not user == None :
    #         return user
    #     # if username in db :
    #     # 	user_data = db[username]
    #     # 	return Customer(user_data)
    #         # return UserInDB(**user_data)

    # def authenticate_user(username : str, password : str) :
    #     user = Customer.get_user(username)
    #     if not user :
    #         return False
    #     if not Customer.verify_password(password, user._password) :
    #         return False
    #     return user

    # def creat_access_token(data : dict, expires_delta : timedelta or None = None) :
    #     encode = data.copy()
    #     if expires_delta != None :
    #         expires = datetime.utcnow() + expires_delta
    #     else :
    #         expires = datetime.utcnow() + timedelta(minutes=5)
    #     encode.update({"exp" : expires})
    #     encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    #     return encode_jwt

    # async def get_current_user(token : str = Depends(OAUTH2_SCHEME)) :
    #     credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate your credentials", headers={"WWW-Authenticate" : "Bearer"})
    #     try :
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         username : str = payload.get("sub")
    #         if username is None :
    #             raise credential_exception
    #         token_data = TokenData(email = username)
    #     except JWTError :
    #         raise credential_exception
    #     user = Customer.get_user(username= token_data.email)
    #     if user is None :
    #         raise credential_exception
    #     return user



    #! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # def request_edit(email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
    # @app.get("/users")
    # async def view_info(self) -> dict:
    #     return (self.__dict__)
    basket = property(get_basket)