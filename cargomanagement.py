class cargosystem:
    def __init__(self,arrival,location):
        self.arrival=arrival
        self.location=location
    def hush(self):
        print("the arrival of your delievery is expected at",self.arrival,"\n","your confirmed  location is",self.location)
class confirmation:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def get(self):
        print("your confirmed name is",self.name,"\n","your confirmed phone number is",self.number)
class clearance:
    def __init__(self,money,accountnumber):
        self.money=money
        self.accountnumber=accountnumber
    def gi(self):
        if self.money==1:
            print("you have selected cash on deliever option")
        elif self.money==2:
            print("you havechossen online money transfer")
   
arrival=input("enter your free time")
location=input("enter your confirmed location")
name=input("enter name")
number=input("enter your number")
print("*press 1 if you wanted cash on delievery option")
print("*press 2 if you wanted onlinemoney transfer")
money=eval(input("enter your desired option"))
accountnumber=input("enter your account number")
print("****AIR CARGO SYSTEM*****")
ob1=cargosystem(arrival,location)
ob1.hush()
ob2=confirmation(name,number) 
ob2.get()
ob3=clearance(money,accountnumber)
print("*press 1 if you wanted cash on delievery option")
print("*press 2 if you wanted onlinemoney transfer")
ob3.gi()
print("___________________________________________________________________________________")


print("**your order will be deliever at your doorstep thankyou for using air cargo system**")

