class UserAccount:
    def __init__(self, email, password, full_name, gender, tel):
        self._email = email
        self._password = password
        self._full_name = full_name
        self._gender = gender
        self._tel = tel

# Inheritance from UserAccount

class Customer(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, address, email_noti, sms_noti):
        super.__init__(self, email, password, full_name, gender, tel)
        self.__address = address
        self.__email_noti = email_noti
        self.__sms_noti = sms_noti

class Admin(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, permission):
        super.__init__(self, email, password, full_name, gender, tel)
        self.__permission = permission