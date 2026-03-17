#now we learn about class methods
#a class method is a type of method that is bound to the class and not instance of the class
#class methods are defined using @classmethods
#for example:-
# class employe:
#     companyname="apple"  #class variabl
#     def info(self,name):
#           self.name=name     
#     def statement(self):
#             print(f"my name is : {self.name} and my company name is: {self.companyname}")

# a=employe()
# a.info("rahul")
# a.statement() #here companyname print apple
# a.companyname="nestle"
# a.info("rohon")
# a.statement() #here company name print nestle due to change
# b=employe()
# b.info("roshon")
# b.statement() #but inthis case company name again print apple 

#but now using class method it parmanently change the value of class variable
class employe:
    companyname="apple"  #class variabl
    def info(self,name):
          self.name=name     
    def statement(self):
            print(f"my name is : {self.name} and my company name is: {self.companyname}")
    @classmethod  #here using class method
    def infoo(self,changecompany):
          self.companyname=changecompany
                

a=employe()
a.info("rahul")
a.statement() #here companyname print apple
a.infoo("nestle")
a.info("rohon")
a.statement() #here company name print nestle due to change
b=employe()
b.info("roshon")
b.statement() #but inthis case company name print nestle because class variable completely change by using @classmethod
