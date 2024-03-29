from Modules.Branch import Branch

# Legacy : Everything in this is exist in BookShop the code also seem outdated. waiting for deletion....

class BranchList():
	def __init__(self):
		self.__list_of_branch = []
		self.__available = []

	@property
	def list_of_branch(self):
		return self.__list_of_branch

	@list_of_branch.setter
	def list_of_branch(self, new_branch):
		self.__list_of_branch = new_branch

	@property
	def available_branch(self):
		return self.__available

	def add_branch(self, branch: Branch):
		self.__list_of_branch.append(branch)

	def delete_branch(self, branch: Branch):
		self.list_of_branch.remove(branch)

	def get_specific_branch(self, Branch):
		for element in self.__list_of_branch:
			if Branch == element._branch_name:
				self.select_branch = element
				return self.select_branch

	def search_available_branch(self, book):
		self.__available = []
		for element in self.__list_of_branch:
			for elements in element._product_in_stock:
				if elements == book:
					self.__available.append(element)

	def search_branch(self, branch):
		self.__available = []
		for element in self.__list_of_branch:
			if branch in element.branch_name:
				self.__available.append(element)
		return (self.__available)
