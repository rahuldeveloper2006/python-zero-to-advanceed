# w programe then a class drives from other class. the child class inherit all the public abd protected properties and methods from the parent class
# in addition , it can have its own properties and method . this is called inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
            print(f"my name is {self.name} and my age is {self.age}")

a=person("rahul kumar bhuyan",19)
a.info()
# if we want to change person tohen we use inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
            print(f"my name is {self.name} and my age is {self.age}")

class programe(person):
     def show(self):
          print("the default langue python")


a=person("rahul kumar bhuyan",19)
a.info()
b=programe("ritik bhuyan",13)
b.show()
b.info()

import math
print(dir(b))