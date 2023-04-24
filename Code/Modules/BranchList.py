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
            
    def search_available_branch(self, book):
        self.__available = []
        for element in self.__list_of_branch:
            for elements in element._product_in_stock:
                if elements == book:
                    self.__available.append(element)
    
    def select_branch(self, branch_name):
        for i in self.__list_of_branch:
            if branch_name == i._branch_name:
                select_branch = i
        return select_branch

    def get_list(self):
        return self.__list_of_branch
    
    def set_list(self,new_branch):
        self.__list_of_branch = new_branch
        
    def get_available(self):
        return self.__available
    
    list_of_branch = property(get_list, set_list)
    available_branch = property(get_available)
