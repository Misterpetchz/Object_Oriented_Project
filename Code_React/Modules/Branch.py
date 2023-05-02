from Modules.Book import Book


class Branch():
	def __init__(self, branch_name, open_time, location, tel, line_id, facebook_id):
		self.__branch_name = branch_name
		self.__open_time = open_time
		self.__location = location
		self.__tel = tel
		self.__line_id = line_id
		self.__facebook_id = facebook_id
		self.__product_in_stock = []

	def add_product(self, book):
		self.__product_in_stock.append(book)

	@property
	def branch_name(self):
		return self.__branch_name

	@branch_name.setter
	def branch_name(self, a):
		self.__branch_name = a

	@property
	def open_time(self):
		return self.__open_time

	@open_time.setter
	def open_time(self, a):
		self.__open_time = a

	@property
	def location(self):
		return self.__location

	@location.setter
	def location(self, a):
		self.__location = a

	@property
	def tel(self):
		return self.__tel

	@tel.setter
	def tel(self, a):
		self.__tel = a

	@property
	def line_id(self):
		return self.__line_id

	@line_id.setter
	def line_id(self, a):
		self.__line_id = a

	@property
	def facebook_id(self):
		return self.__facebook_id

	@facebook_id.setter
	def facebook_id(self, a):
		self.__facebook_id = a

	@property
	def product_in_stock(self):
		return self.__product_in_stock

	@product_in_stock.setter
	def product_in_stock(self, a):
		self.__product_in_stock = a

	def modify_branch(self, new_branch_name, new_open_time, new_location, new_tel, new_line_id, new_facebook_id, list_add_book, list_delete_book):
		if isinstance(new_branch_name, str):
			if new_branch_name != '':
				self.__branch_name = new_branch_name
		if isinstance(new_open_time, str):
			if new_open_time != '':
				self.__open_time = new_open_time
		if isinstance(new_location, str):
			if new_location != '':
				self.__location = new_location
		if isinstance(new_tel, str):
			if new_tel != '':
				self.__tel = new_tel
		if isinstance(new_line_id, str):
			if new_line_id != '':
				self.__line_id = new_line_id
		if isinstance(new_facebook_id, str):
			if new_facebook_id != '':
				self.__facebook_id = new_facebook_id
		if isinstance(list_add_book, list):
			for book in list_add_book:
				if book not in self.__product_in_stock:
					self.__product_in_stock.append(book)
		if isinstance(list_delete_book, list):
			for book in list_delete_book:
				self.__product_in_stock.remove(book)

	def add_book_to_stock(self, book: Book):
		if book not in self.__product_in_stock:
			self._product_in_stock.append(book)

	def find_book_in_stock(self, book_name):
		for book in self._product_in_stock:
			if book_name == book._name:
				return book

	def remove_book_from_stock(self, book: Book):
		if book in self._product_in_stock:
			self._product_in_stock.remove(book)
