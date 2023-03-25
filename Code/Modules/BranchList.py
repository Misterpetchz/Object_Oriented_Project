from Modules.Branch import Branch
class BranchList():
    def __init__(self, list_of_branch):
        self.__list_of_branch = list_of_branch
        
    def remove_branch(Branch):
        pass
    def get_specific_branch(self,Branch):
        for element in self.__list_of_branch:
            if Branch == element._branch_name:
                self.select_branch = element
                return self.select_branch
            
    def get_list(self):
        return self.__list_of_branch
    def set_list(self,new_branch):
        self.__list_of_branch = new_branch
    list_of_branch = property(get_list, set_list)