#static method in python it belongs in a class , it is using by @static method
#some example:-
#if we wants sum operation do in a class 
# class values:
#     def __init__(self,value):
#         self.value=value
#     def sum(self,n):
#             self.value=self.value+n
#             print(self.value)
# a=values(12)
# a.sum(12)
#but it is difficult so here we use static method
class values:
    def __init__(self,value):
        self.value=value
    def sum(self,n):
            self.value=self.value+n
            print(self.value)
    @staticmethod
    def add(x,y):
                 print(x+y)
    @staticmethod
    def mul(a,b):
           print(a*b)
a=values(12)
a.sum(12)
a.add(12,12) #this is the static method 
#static method is used to perform a operation and drive a function in a class without use self argument
a.mul(12,2)