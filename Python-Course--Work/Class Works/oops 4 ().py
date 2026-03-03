# Encapsulation = Wrapping data (variables) and methods into a single unit (class) and protecting the data from outside access.
# In simple words:Hide the internal details and show only what is necessary.
# Real-life example 🏧
# Think of an ATM:
# You can withdraw money
# You cannot directly access the bank server or balance variables
# That protection = Encapsulation

# 1.
class Facebook:
    def __init__(self,username,password,profilepic):
        self.username=username
        self.__password=password
        self._profilepic=profilepic
    def getpwd(self):
        return self. __password
    def setpwd(self,newpwd):
        self. __password=newpwd
        
subhash=Facebook('subhash','123456','subbu.png')
print("befor:{'subhash.username}")
subhash.username="venkata"
print(f"after:{subhash.username}")
print(f'\n before:{subhash.getpwd()}')
subhash.setpwd("S@123")
print(f'after:{subhash.getpwd()}')