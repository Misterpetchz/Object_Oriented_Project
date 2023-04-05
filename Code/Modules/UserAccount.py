	#? Module
from Modules.Basket import Basket
from Modules.Catalog import Catalog
from Modules.Book import BookItem
from Modules.Branch import Branch
from Modules.BranchList import BranchList
	#? External Lib
from Modules.main import *

class UserAccount:
	def __init__(self, email, password, full_name, gender, tel):
		self._email = email
		self._password = password
		self._full_name = full_name
		self._gender = gender
		self._tel = tel

# Inheritance from UserAccount
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

class Customer(UserAccount):
	# def __init__(self, email, password, full_name, gender, tel, address, email_notification, sms_notification):
	def __init__(self, data_dict : dict):
		super().__init__(data_dict["_email"], data_dict["_password"], data_dict["_full_name"], data_dict["_gender"], data_dict["_tel"])
		self._address = data_dict["_address"]
		self._email_notification = data_dict["_email_notification"]
		self._sms_notification = data_dict["_sms_notification"]
		self.__basket = Basket([])
		self._disabled = False
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

	def request_edit() :
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

	#! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	def verify_password(plain_password, hashed_password) :
		return PWD_CONTEXT.verify(plain_password, hashed_password)

	def get_password_hash(password) :
		return PWD_CONTEXT.hash(password)

	def get_user(db, username : str) :
		user = InstanceFinder(Customer, "_email", username)
		if not user == None :
			return user
		# if username in db :
		# 	user_data = db[username]
		# 	return Customer(user_data)
			# return UserInDB(**user_data)

	def authenticate_user(db, username : str, password : str) :
		user = Customer.get_user(db, username)
		if not user :
			return False
		if not Customer.verify_password(password, user._password) :
			return False
		return user

	def creat_access_token(data : dict, expires_delta : timedelta or None = None) :
		encode = data.copy()
		if expires_delta != None :
			expires = datetime.utcnow() + expires_delta
		else :
			expires = datetime.utcnow() + timedelta(minutes=5)
		encode.update({"exp" : expires})
		encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
		return encode_jwt

	async def get_current_user(token : str = Depends(OAUTH2_SCHEME)) :
		credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate your credentials", headers={"WWW-Authenticate" : "Bearer"})
		try :
			payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
			username : str = payload.get("sub")
			if username is None :
				raise credential_exception
			token_data = TokenData(email = username)
		except JWTError :
			raise credential_exception
		user = Customer.get_user(db, username= token_data.email)
		if user is None :
			raise credential_exception
		return user



	#! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# def request_edit(email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
	# @app.get("/users")
	# async def view_info(self) -> dict:
	#     return (self.__dict__)
	basket = property(get_basket)


async def get_current_active_user(current_user : Customer = Depends(Customer.get_current_user)) :
	# print(current_user.__dict__)
	# if current_user._disabled :
	# 	raise HTTPException(status_code=400, detail="Inactive User")
	return current_user

@app.put("/users/edit")
async def info_verification(email : Optional[str] = None, password : Optional[str] = None, full_name : Optional[str] = None, gender : Optional[str] = None, tel : Optional[str] = None, address : Optional[str] = None,
				email_noti : Optional[bool] = None, sms_noti : Optional[bool] = None, id : Customer = Depends(Customer.get_current_user)) :
	if (id == None) :
		return {"Error-101" : "Didn't find any account with this id"}
	id._email = email or id._email
	id._password = password or id._password
	id._full_name = full_name or id._full_name
	id._gender = gender or id._gender
	id._tel = tel or id._tel
	id._address = address or id._address
	id._email_notification = email_noti if email_noti != None else id._email_notification
	id._sms_notification = sms_noti if sms_noti != None else id._sms_notification

@app.post("/token", response_model=Token)
async def login(form_data : OAuth2PasswordRequestForm = Depends()) :
	user = Customer.authenticate_user(db, form_data.username, form_data.password)
	if not user :
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password", headers={"WWW-Authenticate" : "Bearer"})
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
	access_token = Customer.creat_access_token(data={"sub" : user._email}, expires_delta=access_token_expires)
	return {"access_token" : access_token, "token_type" : "bearer"}

@app.get("/users/me")
async def view_info(userid : Customer = Depends(get_current_active_user)):
	# id = InstanceFinder(Customer, "_email", userid)
	# if (id == None) :
	# 	return {"Error-101" : "Didn't find any account with this id"}
	# else :
		return (userid)
