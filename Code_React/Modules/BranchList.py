from Modules.Branch import Branch
class BranchList():
	def __init__(self):
		self.__list_of_branch = []
		self.__available = []

	def add_branch(self, branch:Branch):
		self.__list_of_branch.append(branch)

	def delete_branch(self, branch:Branch):
		self.list_of_branch.remove(branch)

	def get_specific_branch(self,Branch):
		for element in self.__list_of_branch:
			if Branch == element._branch_name:
				self.select_branch = element
				return self.select_branch

	def search_branch(self, branch) :
		self.__available = []
		for element in self.__list_of_branch :
			if branch in element.branch_name :
				self.__available.append(element)
		return (self.__available)

	def get_list(self):
		return self.__list_of_branch

	def set_list(self,new_branch):
		self.__list_of_branch = new_branch

	def get_available(self):
		return self.__available

	list_of_branch = property(get_list, set_list)
	available_branch = property(get_available)
