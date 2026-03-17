#multilevel inheritance is a types of inheritance where a derived class inherites from another derived class
#some example:-
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def statement1(self):
        print(f"animal name is {self.name}")
        print(f"animal's species is {self.species}")
class cat(animal):
    def __init__(self,name,voice):
        animal.__init__(self,name,species="cat")
        self.voice=voice
    def statement2(self):
        animal.statement1(self)
        print(f"cat's voice is{self.voice} ")
class dog(cat):
    def __init__(self,name,colour):
        cat.__init__(self,name,voice="meaunn")
        self.colour=colour
    def statement3(self):
        cat.statement2(self)
        print(f"dog's  colour is {self.colour}")
o=dog("tommy","black")
o.statement3()