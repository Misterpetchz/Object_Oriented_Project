from Modules.Branch import Branch
class BranchList():
    def __init__(self):
        self.__list_of_branch = []
    
    def add_branch(self, branch):
        if isinstance(branch,Branch):
            self.list_of_branch.append(branch)
        
    def delete_branch(self, branch:Branch):
        self.list_of_branch.remove(branch)

    def get_list(self):
        return self.__list_of_branch
    def set_list(self,new_branch):
        self.__list_of_branch = new_branch
    list_of_branch = property(get_list, set_list)