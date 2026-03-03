#without constructor in python
class Flipkart:
    def userinfo(self, name, password, mobileno):
        self.name = name
        self.password = password
        self.mobileno = mobileno

        print(f"UserInfo:\nName: {self.name}\nPassword: {self.password}\nMobile No: {self.mobileno}")

ajay = Flipkart()
rupak = Flipkart()

ajay.userinfo("Ajay", "1234", "59876543210")
rupak.userinfo("Rupak", "1234", "8765432109")

# with constructor in python 

class Flipkart:
    def __init__(self, name, password, mobileno):
        self.name = name
        self.password = password
        self.mobileno = mobileno

        print(f"UserInfo:\nName: {self.name}\nPassword: {self.password}\nMobile No: {self.mobileno}")

ajay1 = Flipkart("Ajay", "1234", "9876543210")
rupak = Flipkart("Rupak", "1234", "8765432109")

class Flipkart:
    discount = 10  # class variable

    @classmethod
    def set_discount(cls):
        print(cls.discount)
    
    @staticmethod
    def banner():
        print(''' Flipkart Buy-1 Get-1 sale is going on. \nshop now!''')
    
    def __init__(self, name, password, mobileno):
        self.name = name
        self.password = password
        self.mobileno = mobileno

        print(f"UserInfo:\nName: {self.name}\nPassword: {self.password}\nMobile No: {self.mobileno}")

Dhanush = Flipkart("Dhanush", "7657cuiuahcuia", "9876456467576543210")
Abhinov = Flipkart("Abhinov", "ggajgjbhjx565", "87654674876855732109")

Flipkart.banner()
Dhanush.banner()

Flipkart.set_discount()
Dhanush.set_discount()

