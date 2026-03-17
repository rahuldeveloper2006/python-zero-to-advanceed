#class is blueprint or template for creating object providing initial value
# class person:
#     name="rahul kumar bhuyan"
#     age=19
#     occu="software developer"
#     def info(self):
#         print(f"iam {self.name} iam {self.age} years old and my occupation is {self.occu}")
    
# a=person() #now we create a object name is "a"
# print(a.name) #print rahul kumar bhuyan
# a.info() #here the object call the info function and print the block of code
# #if we wants to change the person's name , occu and age then
# a.name='rohon'
# a.age=18
# a.occu="doctor"
# a.info()  # here print new data instead of old data
# b=person()
# b.name="ritik"
# b.info() #here only change name but it print occu and age by default 19 and software developer
# #now we learn "self paramerter"
# #the self parameter is a reference to the current inctance of the class and is used to access variables that belongs to the class.
# #it must be provides extra parameter inside the method defination
#example
class students:
    name="rahul kumar bhuyan"
    rollno=155
    clas="btech"
    def info(self):
        print(f"my name is {self.name} and my rollno {self.rollno} a in study in {self.clas}")
abj=students()
abj.info()
