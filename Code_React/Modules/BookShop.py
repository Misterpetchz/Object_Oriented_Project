from Modules.Branch import Branch
from Modules.EventDiscount import EventDiscount
from Modules.Book import Book
import math


class BookShop():
	def __init__(self,event_discount):
		self.__list_of_branch = []
		self.__all_list_of_book = []
		self.__event = event_discount

# + Getter / Setter {START}

	@property
	def list_of_branch(self):
		return self.__list_of_branch

	@list_of_branch.setter
	def list_of_branch(self, new_branch):
		self.__list_of_branch = new_branch

	@property
	def list_all_of_book(self):
		return self.__all_list_of_book

	@list_all_of_book.setter
	def list_all_of_book(self, new_list):
		self.__all_list_of_book = new_list
  
	@property
	def event(self):
		return self.__event
	@event.setter
	def event(self,new_event):
		self.__event = new_event

# + Getter / Setter {END}

# Description : Add branch to the list of all branch
	def add_branch(self, branch: Branch):
		self.__list_of_branch.append(branch)

# Description : Delete branch from list of all branch
	def delete_branch(self, branch_name: str):
		for element in self.__list_of_branch:
			if branch_name == element.branch_name:
				self.__list_of_branch.remove(element)

# Description : Reture infomation of the branch with the same name as input
	def select_branch(self, branch_name):
		for element in self.__list_of_branch:
			if branch_name == element.branch_name:
				select_branch = element
				return select_branch

# Description : Search for the branch that has book as the same name as input
# * DUPLICATE FUNCTION : 01
	def search_available_branch(self, book_name):
		available = []
		for element in self.__list_of_branch:
			for elements in element.product_in_stock:
				if book_name == elements.name:
					available.append(element)
		return available

# Description : Return list of the branch that have input string in its name
	def search_branch(self, branch_name):
		available = []
		for element in self.__list_of_branch:
			if branch_name.lower() in element.branch_name.lower():
				available.append(element)
		return available

# Description : Add new book to the database
	def add_book(self, book):
		self.__all_list_of_book.append(book)
		self.apply_discount()

# Description : Find book that has EXACTLY the same name as input
	def find_book_by_name(self, name):
		for i in self.list_all_of_book:
			if name == i.name:
				return i

# Description : Return list of book that has the input string in its name
	def search_book(self, search_string):
		list_of_book = []
		for element in self.__all_list_of_book:
			if search_string.lower() in element.name.lower():
				list_of_book.append(element)
		return list_of_book

# Description : Remove book from the database
	def remove_book(self, book):
		for element in self.__all_list_of_book:
			if book == element:
				self.__all_list_of_book.remove(element)

# Description : Return list of branch that has book which have input string in it
# * DUPLICATE FUNCTION : 01
	def check_stock(self, book_name):
		list = []
		for branch in self.__list_of_branch:
			if book_name in [book.name for book in branch.product_in_stock]:
				list.append(branch)
		return list

# Description : Apply discount to all book in database
	def apply_discount(self):
		for i in self.__all_list_of_book:
			if self.__event.event_genre in i.genre:
				i.new_price = math.floor(int(i.price) * self.__event.discounted_percentage)
