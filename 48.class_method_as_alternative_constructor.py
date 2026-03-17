#now we learn class method as alternative constructor
#some example
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# a=person("rahul kumar bhuyan","55")
# print(a.name)
# print(a.age)
# # but we neter input in string method
# string="rahul kumar bhuyan-55"
# b=person(string.split("-")[0],string.split("-")[1])
# print(b.name)
# print(b.age)
#but we use this split method in class
class about:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"my name is {self.name} and my age is {self.age}")
    @classmethod
    def from_string(self,string):
        return self(string.split("-")[0],string.split("-")[1])
        
# a=about("rahul",12)
# a.info()
string="rohon bhuyan-19"
b=about(string)
print(b.name)
print(b.age)
