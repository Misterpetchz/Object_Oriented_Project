from Modules.Branch import Branch
from Modules.EventDiscount import EventDiscount
class BookShop():
    def __init__(self):
        self.__list_of_branch = []
        self.__list_of_event = []
        self.__available = []
    
    # Getter % Setter
    @property
    def list_of_branch(self):
        return self.__list_of_branch
    
    @list_of_branch.setter
    def list_of_branch(self, new_branch):
        self.__list_of_branch = new_branch

    @property
    def list_of_event(self):
        return self.__list_of_event
    
    @list_of_event.setter
    def list_of_event(self, new_event):
        self.__list_of_event = new_event

    @property
    def available(self):
        return self.__available
    
    # Branch List
    def add_branch(self, branch:Branch):
        self.__list_of_branch.append(branch)
    
    def delete_branch(self, branch:Branch):
        self.__list_of_branch.remove(branch)

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
    
    def search_available_branch(self, book):
        self.__available = []
        for element in self.__list_of_branch:
            for elements in element._product_in_stock:
                if elements == book:
                    self.__available.append(element)
        return self.__available
    
    # Event List
    def add_event(self, event:EventDiscount):
        self.__list_of_event.append(event)

    def delete_event(self, event:EventDiscount):
        self.__list_of_event.remove(event)

    def select_event(self, event_name):
        for element in self.__list_of_event:
            if event_name == element.event_name:
                select_event = element
                return select_event
    