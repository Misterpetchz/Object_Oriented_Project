from Modules.Branch import Branch
class BranchList():
    def __init__(self):
        self.__list_of_branch = []
    
    def add_branch(self, branch):
        if isinstance(branch,Branch):
            self.list_of_branch.append(branch)
        
    def delete_branch(self, branch:Branch):
        self.list_of_branch.remove(branch)

    def select_branch(self, branch_name):
        for i in self.__list_of_branch:
            if branch_name == i._branch_name:
                select_branch = i
        return select_branch

    def get_list(self):
        return self.__list_of_branch
    def set_list(self,new_branch):
        self.__list_of_branch = new_branch
    list_of_branch = property(get_list, set_list)