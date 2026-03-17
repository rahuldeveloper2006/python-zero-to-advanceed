#difference between class variable and instance variable are:
#if we change class variable the the vaeiable change for all call
#but if we change instance variable then it can change only for that which is called
class person:
    companyname="apple"    #class variable
    def __init__(self,name):
        self.name=name    #instance variable
    def full(self):
            print(f"my name is {self.name} and i work in {self.companyname}")
a=person("rahul")
# a.full() 
b=person("rohon")
# b.full()
# a.companyname="google" # here we change class variable by using object "a"it can change only for that object which is called
# a.full()
# b.full() #here b is not change it print the same value apple
# #if we change the class variable by using class
person.companyname="nestle" #here change the class variable for all 
a.full()
b.full()