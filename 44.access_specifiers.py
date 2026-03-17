#access specifier in python is used to limit the access of vaeiables and method of class
#types of access specifiers:
#1. public acces modifier 2. private access modifier  3.protected access modifier
#public access modifier means we can access the class variables out sidethe class
# class person:
#     def __init__(self,):
#         self.name="rahul kumar bhuyan"  #public variables
#         self.age=19
# obj=person()
# print(obj.name)
# print(obj.age) # we can access 

#private modifier means we cannot access the class variables out side the class
# class myclass:
#     def __init__(self):
#         self.__name="rahul kumar bhuyan"  #private variables
#         self._age=19
# obj=myclass()
# # print(obj.__name)   # we cannot access here directly so it is private modifier
# print(obj._age) # we can access directly bcz it is a public variable
# #but we can access indirectly by using "name mangling"
# print(obj._myclass__name) #now we access indirectly
# print(obj._age)

#protected access modifier
class person:
    def __init__(self):
        self._name="rahul kumar bhuyan"
    def _funname(self):
            return "ritik bhuyan"
    
class employe(person):   #using inheritance
     pass
obj=person()
obj1=employe()
print(obj._name)
print(obj._funname())
print(obj1._name)
print(obj1._funname())