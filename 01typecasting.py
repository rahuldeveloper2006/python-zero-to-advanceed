#type conversion
# #type conversion means the data type automatically change to our desire datatype
# ex:-
a=23
b=23.45
print(a+b)
print(type(a+b))  #her the data type automatically change from int to float

#type casting
#type casting means -the data type not change automatically to desire data type,it changes mannually
# ex:-
a=float(2)
b=4.25
print(type(a))
print(type(a+b),a+b)
#now we write a program in case of my own biodata
name=input("enter your name")
clas=input("enter your course")
rollno=input("enter your roll number")
age=input("enter your age")
print("my name is:",name)
print("my clas is:",clas)
print("my roll number is:",rollno)
print("my age is:",age)
#explicit typecasting means by user
#implicit typecasting means by python
a=26
b=56.23
print(a+b)
