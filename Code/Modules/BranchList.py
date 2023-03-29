from Modules.Branch import Branch
class BranchList():
    def __init__(self, list_of_branch):
        self.__list_of_branch = list_of_branch
        self.__available = []
    def remove_branch(Branch):
        pass
    def modify_branch(Branch):
        pass
    def add_branch(self, branch):
        if isinstance(branch, Branch):
            self.list_of_branch.append(branch)
    def search_available_branch(self, book):
        self.__available = []
        for element in self.__list_of_branch:
            for elements in element._product_in_stock:
                if elements == book:
                    self.__available.append(element)
    def get_list(self):
        return self.__list_of_branch
    def set_list(self,new_branch):
        self.__list_of_branch = new_branch
    def get_available(self):
        return self.__available
    list_of_branch = property(get_list, set_list)
    available_branch = property(get_available)