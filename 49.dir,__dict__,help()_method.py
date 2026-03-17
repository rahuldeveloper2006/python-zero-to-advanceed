#now we study different methods
#dir() function show all the methods and attributes of list,tuples,and other.........
a=[12,32,34]
print(dir(a))
b=(12,34)
print(dir(b))  #print all attributes and methods of tuples

#now we learn __dict__ method
#__dect__ method help to show all items in dictionary and class
class employe:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
ai=employe("rahul",55)
print(ai.__dict__)

#now we learn help() method
#help() method it helps to show documentatoion of object
# list=[12,34]
# print(help(list))
print(help(tuple))
# print(string)