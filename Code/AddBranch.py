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
pookan_admin555.add_branch(all_branch, nonthaburi1)
print(all_branch.list_of_branch[0]._branch_name)