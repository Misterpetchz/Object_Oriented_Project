from dataclasses import dataclass

@dataclass
class Book :

    name : str
    price : float = 0.00
    
    def Passing(self) :
        pass


class Catalog :

    def __init__(self) :
        self.log = []

    def add_book(self, book) :
        self.log.append(book)

    def get_book(self, book_name) :
        for book in self.log :
            if book.name == book_name :
                rtn_book = book
                self.log.remove(book)
                return (rtn_book)

        return (None)

class Basket :
    def __init__(self) :
        self.log = []
    def add_to_list(self, book) :
        self.log.append(book)

class Customer :

    def __init__(self, name) :
        self.name = name
        self.basket = Basket()

    def add_basket(self, book_name) :
        result = catalog1.get_book(book_name)

        if result != None :
            self.basket.add_to_list(result)
            print("Ayin add " + bookname + " to the basket.")
        else :
            print("No book left!")


catalog1 = Catalog()
# catalog1.add_book(Book(name="A", price=159.00))
# catalog1.add_book(Book(name="B", price=129.00))
# catalog1.add_book(Book(name="C", price=149.00))
customerA = Customer("Ayin")
# print("Ayin add A to basket")
# customerA.add_book_to_basket("A")
# print(catalog1.log)
# print(customerA.basket.log)
# print("Ayin add C to basket")
# customerA.add_book_to_basket("C")
# print(catalog1.log)
# print(customerA.basket.log)
# print("Ayin add D to basket")
# customerA.add_book_to_basket("D")
# print(catalog1.log)
# print(customerA.basket.log)
def add_to_catalog(bookname, price) :
    catalog1.add_book(Book(name=bookname, price=price))
    print("The book " + bookname + " has been added to catalog.")
    print("Now the catalog has " + str(catalog1.log))

def add_book_to_basket(bookname) :
    customerA.add_basket(bookname)
    print("Now the catalog has " + str(catalog1.log))
    print("And the basket has " + str(customerA.basket.log))

while True :
    mode = 'm'
    mode = input('select your mode (b, a) : ')
    while mode == 'a' : 
        bookname = input('enter your book name : ')
        price = input('enter your price : ')
        add_to_catalog(bookname, price)
        mode = 'm'
    while mode == 'b' :
        bookname = input('enter your book name : ')
        add_book_to_basket(bookname)
        mode = 'm'

    if mode != 'a' and mode != 'b' :
        mode = 'm'




