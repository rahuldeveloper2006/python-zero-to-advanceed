#a constructor is a special method in a class it is used to intialize and create an object of a class
#some example
#default constructor
# class person:
#     def __init__(self):
#         print("rahul is a good boy")
# a=person() #when we create an object then the constructor function call
#two types of constructor are available
#there are 1. parameterized constructor and other is 2. default constructor
#parameterized constructor
#it take more than one arguments 
class persons:
   def __init__(self,name,rollno):
       self.name=name
       self.rollno=rollno
   def info(self):
           print(f"my name  is {self.name} and my rollno is {self.rollno}")
a=persons("rahul",55) #here call the function and also pass the arguments
a.info()
b=persons("puja",52)
b.info()

