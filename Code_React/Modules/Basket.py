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
  
	def add_book_to_basket(self, book_item, book: Book):
		if book.stock_amount > 0:
			for i in self.__book_item:
				if i.name.lower() == book_item.name.lower():
					i.amount = i.amount + 1
					book.stock_amount -= 1
					self.__price += book_item.price
					return None
			else:
				self.add_book(book_item)
				book.stock_amount -= 1
				self.__price += book_item.price

	def reduce_amount(self, book_item, book: Book):
		for item in self.__book_item:
			if book_item == item.name:
				item.amount = item.amount-1
				book.stock_amount += 1
				self.__price -= item.price
				if item.amount == 0:
					self.__book_item.remove(item)

	def add_amount(self, book_item, book: Book):
		if book.stock_amount > 0:
			for item in self.__book_item:
				if book_item == item.name:
					item.amount = item.amount+1
					book.stock_amount -= 1
					self.__price += item.price

	def delete_item(self, book_item, book: Book):
		for item in self.__book_item:
			if book_item == item.name:
				book.stock_amount += item.amount
				self.__book_item.remove(item)
