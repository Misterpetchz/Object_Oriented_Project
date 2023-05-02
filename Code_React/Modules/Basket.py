from Modules.Catalog import *


class Basket:
	def __init__(self):
		self.__book_item = []
		self.__price = 0

# + Getter / Setter {START}

	@property
	def book_item(self):
		return self.__book_item

	@book_item.setter
	def book_item(self, new_book_item):
		self.__book_item = new_book_item

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, new_price):
		self.__price = new_price

# + Getter / Setter {END}

# Description : Add book to basket
	def add_book(self, book):
		self.__book_item.append(book)
