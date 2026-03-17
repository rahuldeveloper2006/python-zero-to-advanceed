#getters in python are methods that are used to access the values of an object's properties.
#they are used to return the value of specific property and are typically defined using the @property decoreator
# class myclass:
#     def __init__(self,value):
#         self.value=value
#     def show(self):
#         print(f"the value is {self.value}")
#     @property
#     def tentimes(self):
#      return 10*self.value
# a=myclass(10)
# print(a.tentimes) #here increse the self.value in ten times i.e 10 to 100
# a.show()

#setters in python
#getters do not take any parameters and we canot set the value through getter method. for that we need setter method wwhich can 
#be adde by decorating method with 

# class values:
#    def __init__(self,value):
#       self.value=value
#    def info(self):
#       print(f"the value is :{self.value}")
#    @property
#    def tentimes(self):
#          return 10*self.value
#    @tentimes.setter
#    def tentimes(self,newvalue):
#       self.value=newvalue
# obj=values(10)
# obj.info()
# print(obj.tentimes)
# obj.tentimes=34 #here we can change the value of self.value
# obj.info() 
# #if we want to change the value of self.value then we use setter method. but we can able to use the getter method when we use setter method
# setter method take parameters and change the value but getters are no 


# class person():
#     def __init__(self,value):
#         self.value=value
#     def info(self):
#         print(f"my value is {self.value}") 
#     @property
#     def tentime(self):
#          return 10*self.value
#     @tentime.setter
#     def tentime(self,newvalue):
#       self.value=newvalue
#       print(self.value)
    

# a=person(10)
# a.info()
# print(a.tentime)
# a.tentime=34
# a.info()
# print(a.tentime)


# class identity:
#     def __init__(self,name):
#         self.name=name
#     def info(self):
#         print(f"the name of the student is {self.name}")
    
#     @property
#     def update_name(self):
#         print(self.name)
    
#     @update_name.setter
#     def update_name(self,newname):
#         self.name=newname
        
# obj=identity("Rahul kumar bhuyan")
# obj.info()
# obj.update_name
# obj.update_name="rohon kumar bhuyan"
# obj.update_name
# obj.info()

class Brother:
    def __init__(self):
        self.__name="ritik"
    def show(self):
        print(f"my brother's name is {self.__name}")
    def get_name(self):
        print(self.__name)
    def set_name(self,newname):
        self.__name=newname

a=Brother()
a.show()
# print(a.__name) #create error because we canot direct access the private variables
# a.__name="rahul" #we canot directly modify the private variables
a.set_name("Rahul")
a.get_name()
print(a._Brother__name)
