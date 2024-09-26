class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self):
        total=self.price*self.quantity
        print("Kopējā cena: ",total)


obj1=product("Eļļa",10,4)
obj2=product("Turbīna",100,4)
obj1.get_total_price()
obj2.get_total_price()

class ShoppingCart(product):
    def __init__(self,name,price,quantity):
        super().__init__(name,price,quantity)

    def add_product_to_cart(self):
        print(self.quantity," Produkts/ti ",self.name,"",self.price,"$ pievienots grozam!")

    def remove_product_from_cart(self):
        print("Produkts",self.name," izņemts no groza!")

    def total_total_price(self):
        totaltotal=self.price*self.quantity
        print("Ķopējās izmaksas",totaltotal)



obj1=ShoppingCart("Eļļa",10,4)
IepirkumuGrozs1=obj1
IepirkumuGrozs1.add_product_to_cart()
IepirkumuGrozs1.remove_product_from_cart()
IepirkumuGrozs1.total_total_price()


obj2=ShoppingCart("Turbīna",100,4)
IepirkumuGrozs2=obj2
IepirkumuGrozs2.add_product_to_cart()
IepirkumuGrozs2.remove_product_from_cart()
IepirkumuGrozs2.total_total_price()



class SystemUser:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
    
    def set_user_info(self,newusername,newpassword,newemail):
        print("________________________________________________________")
        print("Vecais info:")
        print("Lietotājvārds: ",self.username)
        print("Lietotāja parole: ",self.password)
        print("Lietotāja e-pasts: ",self.email)
        self.username=newusername
        self.password=newpassword
        self.email=newemail
        
    def get_user_info(self):
        print("________________________________________________________")
        print("Jaunais info:")
        print("Lietotājvārds: ",self.username)
        print("Lietotāja parole: ",self.password)
        print("Lietotāja e-pasts: ",self.email)

Raimonds=SystemUser("Generalis333","Password123","raimondsss@gmail.com")
Raimonds.set_user_info("GeneralBmw","BemWe39m5","raimondsfreaky@hotmail.com")
Raimonds.get_user_info()

