	#!
from Modules.UserAccount import *
from Modules.main import *

# customer1 = Customer("Test1@gmail.com", "1234", "Dante Inferno", "Unknown", "0000000000", "End city 2", True, False)
# customer2 = Customer("Test2@gmail.com", "1234", "Nirvina Lament", "Unknown", "0000000000", "End city 7", True, False)
# customer3 = Customer("Test3@gmail.com", "1234", "Divine Solemn", "Unknown", "0000000000", "End city 0.12", True, False)
# customer4 = Customer("Test4@gmail.com", "1234", "Divine Solemn", "Unknown", "0000000000", "End city 55.12", True, False)
# customer5 = Customer("Test5@gmail.com", "1234", "Divine Solemn", "Unknown", "0000000000", "End city 0.84", True, False)
# customer6 = Customer("Test6@gmail.com", "1234", "Divine Solemn", "Unknown", "0000000000", "End city 3.554", True, False)

customer1 = {
    "_email" : "Test1@gmail.com",
    "_password" : "$2b$12$NYkIOmXIarYOooCQNRmH8uJT1xXOnnJFYYi2tvEm/Gczuu01anm72",
    "_full_name" : "Test 01",
    "_gender" : "Unknown",
    "_tel" : "0000000",
    "_address" : "City 1",
    "__email_notification" : True,
    "__sms_notification" : False
}

customer2 = {
    "_email" : "Test2@gmail.com",
    "_password" : "$2b$12$FNg9XI1nbQxKNA4HUjbUQeHShIGcQfe6BV.Rf/0/50bw5NGzZtCP.",
    "_full_name" : "Test 01",
    "_gender" : "Unknown",
    "_tel" : "0000000",
    "_address" : "City 1",
    "__email_notification" : True,
    "__sms_notification" : False
}

customer3 = {
    "_email" : "Test3@gmail.com",
    "_password" : "$2b$12$UAFcd0LFhSMteVd31fG41eF2KUcoV0DLipTq4Hvnd6sdLCHsMvtiq",
    "_full_name" : "Test 01",
    "_gender" : "Unknown",
    "_tel" : "0000000",
    "_address" : "City 1",
    "__email_notification" : True,
    "__sms_notification" : False
}

customer11 = Customer(customer1)
customer22 = Customer(customer2)
customer33 = Customer(customer3)

dct = {}
lst = ClassInstancePacker(Customer)
for obj in lst :
	dct[obj._email] = obj.toJSON()

with open('data.json', 'w') as f :
	f.write(json.dumps(dct))
