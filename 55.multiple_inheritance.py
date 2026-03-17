#multiple inheritance is a types of inheritance .it is a powerful feature in object oriented programing
# it allows a class inherite property and behaviour from multiple parent classes
#some example
#at first we create multiple classes
class friend:
    def __init__(self,name):
        self.name=name
    def statement(self):
        print(f"my name is : {self.name}")
class favourite():
    def __init__(self,habit):
        self.habit=habit
    def statement2(self):
            print(f"he likes to listening song")
class friend_favourite(friend,favourite):
     def __init__(self,name,habit):
          self.name=name
          self.habit=habit
a=friend_favourite("kiran","song")
a.statement()
a.statement2()
print(a.name)
print(a.habit)
print(friend_favourite.mro())

