
# Polymorphism
class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f"\nHey{self,name}!\nWelcome to the Hotstar")
    def playvideo(self):
        print("Ads will run")
        print("limited access for videos")
        print("limited quality")
        print("speed is limited upto 2x")
        print("background run is not pos1sible")
    def login(self):
        print("limited logins")
    def search(self):
        print("you can search")
    def menu(self):
        print("you can see the menu card")
    def addtofav(self):
        print("you can add movies to the fav list")
class premiumHotstar(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f"Hey{self,name}!\nWelcome to the Hotstar")
    def playvideo(self):
        print("Ads will not run ")
        print("full access for all the videos")
        print("high quality")
        print("speed is upto 4x")
        print("background run is possible")
    def login(self):
        print("multiple logins")
sreehado=premiumHotstar('sreehado')
sreehado.playvideo()
sreehado.login()
sreehado.search()
sreehado.addtofav()
sreehado.menu()
tarak=Hotstar('tarak')
tarak.playvideo()
tarak.login()
tarak.search()
tarak.addtofav()
tarak.menu()


class Number:
    def __init__ (self,num):
        self.num = num
    def ___add___(self,other):
        return self.num+other.num
    def ___sub___(self,other):
        return self.num-other.num
    def ___mul___(self,other):
        return self.num*other.num
    def ___floordiv___(self,other):
        return self.num//other.num

n1 = (20)
n2 = (10)

print (n1+n2)
print (n1-n2)
print (n1*n2)
print (n1//n2)



