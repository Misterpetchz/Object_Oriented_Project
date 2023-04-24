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
			for i in self.__basket.book_item:
				if i.name.lower() == book_item.name.lower():
					i.amount = i.amount + 1
					book._amount_in_stock -= 1
					self.__basket.price += book_item._price
					return None
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
		if book.stock_amount > 0:
			for item in self.basket.book_item:
				if book_item == item.name:
					item.amount = item.amount+1
					book.stock_amount -=1
					self.basket.price += item.price

	def delete_item(self,book_item,book:Book):
		for item in self.basket.book_item:
			if book_item == item.name:
				book.stock_amount += item.amount
				self.basket.book_item.remove(item)

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
	# ? GETTER // SETTER ############################################################
	def add_order_to_order_list(self, order):
		self.__order_list.append(order)

	def update_order_id(self):
		self.__order_id += 1

	def reset_payment(self):
		self.__payment = None
		self.__payment_id = None
		self.__order = None

	@property
	def basket(self):
		return self.__basket
	@property
	def order_list(self):
		return self.__order_list
	@property
	def order_id(self):
		return self.__order_id
	@property
	def email_notification(self):
		return self.__email_notification
	@property
	def sms_notification(self):
		return self.__sms_notification
	@email_notification.setter
	def email_notification(self, value):
		self.__email_notification = value
	@sms_notification.setter
	def sms_notification(self, value):
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
	#################################################################################
	def toJSON(self) :
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
		pass
