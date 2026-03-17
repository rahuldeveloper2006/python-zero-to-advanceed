#single inheritance is a types of inheritance where a class inherite behaviour and properties from a single parent calss
#for example:-
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def animal_sound(self):
            print("the sound of animal")
class cat(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="cat")
        self.breed=breed
    def cat_sound(self):
            print(f"the cat sound is meaunnnn")
a=cat("cat","domestic animal")
a.cat_sound()
a.animal_sound()
print(a.name)
print(a.species)
print(a.breed)