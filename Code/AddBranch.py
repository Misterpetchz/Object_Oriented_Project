from Modules.UserAccount import Admin
from Modules.Book import Book
from Modules.BranchList import BranchList
from Modules.Branch import Branch

nonthaburi1 = Branch("Nonthaburi",
                     "8:30-22:00",
                     "Nonthaburi",
                     "0811111111",
                     "seed_nonthaburi01",
                     "NonthaburiSE-ED",
                     )

all_branch = BranchList()
all_branch.add_branch(nonthaburi1)
catalog = all_branch.list_of_branch
print(catalog)