class UserAccount:
    def __init__(self, email, password, full_name, gender, tel , shipping):
        self._email = email
        self._password = password
        self._full_name = full_name
        self._gender = gender
        self._tel = tel
        self._shipping = shipping

# Inheritance from UserAccount

class Customer(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, shipping, address, email_notification, sms_notification):
        super().__init__(email, password, full_name, gender, tel, shipping)
        self._address = address
        self.__email_notification = email_notification
        self.__sms_notification = sms_notification

class Admin(UserAccount):
    def __init__(self, email, password, full_name, gender, tel, shipping, permission):
        super().__init__(email, password, full_name, gender, tel, shipping)
        self.__permission = permission