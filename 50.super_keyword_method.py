#now we learn about super() keyword
#super() keyword it help to jump the exicution on upper level
class parentclass:
    def parentmethod(self):
        print("iam a parent method")
class childclass(parentclass):
    def parentmethod(self):
        print("iam a another parent method")
        super().parentmethod()
    def childmethod(self):
        print("iam a child method")
        super().parentmethod()     #super() function having self argument in hide so we cannot define self when super() call
a=childclass()
a.childmethod()
a.parentmethod()

#another example of super keyword
class employe:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def statement(self):
            print(f"my name is  {self.name} and my age is{self.age}")
class programer(employe):
     def __init__(self,name,age,lang):
          super().__init__(name,age)
          self.lang=lang
rahul=employe("rahul kumar bhuayn",19)
rohon=programer("rohon kumar bhuyan",17,"python")
rohon.statement()
print(rohon.age)
print(rohon.name)


