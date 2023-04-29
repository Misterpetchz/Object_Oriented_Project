from Modules.Branch import Branch
from Modules.EventDiscount import EventDiscount
from Modules.Book import Book
class BookShop():
	def __init__(self):
		self.__list_of_branch = []
		self.__all_list_of_book = []

	# Getter % Setter
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
	def list_all_of_book(self,new_list):
		self.__all_list_of_book = new_list

	# Branch List
	def add_branch(self, branch:Branch):
		self.__list_of_branch.append(branch)

	def delete_branch(self, branch_name:str):
		for element in self.__list_of_branch:
			if branch_name == element._branch_name:
				self.__list_of_branch.remove(element)

	def select_branch(self, branch_name):
		for element in self.__list_of_branch:
			if branch_name == element._branch_name:
				select_branch = element
				return select_branch

	def get_specific_branch(self,Branch):
		for element in self.__list_of_branch:
			if Branch == element._branch_name:
				self.select_branch = element
				return self.select_branch

	def search_available_branch(self, book_name):
		self.__available = []
		for element in self.__list_of_branch:
			for elements in element._product_in_stock:
				if book_name == elements._name :
					self.__available.append(element)
		return self.__available

	def search_branch(self,branch_name):
		available=[]
		for element in self.__list_of_branch:
			if branch_name in element.branch_name:
				available.append(element)
		return available

	#Catalog
	def add_book(self, book):
		self.__all_list_of_book.append(book)
  
	def find_book_by_name(self, name):
		for i in self.list_all_of_book:
			if name == i._name:
				return i

	def search_book(self, search_string):
		self.__list_of_book = []
		for element in self.__all_list_of_book:
			if search_string in element._name:
				self.__list_of_book.append(element)