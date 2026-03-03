class instagram:
    settings=['visi','priv','....']
    pass
subhash=instagram()
venkata=instagram()

# 3. Design a class to represent a Flipkart user and print user information using a class method.

class Filpkart:
    def userinfo(self,name,password,mobileno):
        self.name=name
        self.password=password
        self.mobileno=mobileno
        print(f"userinfo:\nName:{self.name}\npassword:{self.password}\nmobile no:{self.mobileno}")
subhash=Filpkart()
subhash.userinfo("sai123","sai@123",9876543213)