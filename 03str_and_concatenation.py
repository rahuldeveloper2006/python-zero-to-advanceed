#string is nothing ,it is a sequence of charecter which is initiate from null,it is also a data type
#ex:-
str=input("enter your name")
print(str)
print(type(str))
print(len(str))
print(str[2])#this is the form of index which initiate from 0
about="""my name is rahul kumar bhuyan
my father's name sahadev bhuyan
my mother's name is ranjita bhuayn
my brother's name is ritik bhuyan"""
print(about)
print(len(about))
#now we using for loop in string for print the all charecter in sequence
for i in about:
    print(i)
#cocatenation
#concatenation means-adding of two string value
#ex:-
str1=(input("enter your name"))
str2=(input("enter your title"))
print(type(str1+str2),str1+str2)
#concatenation
strr1='rahul'
strr='bhuyan'
print(strr1+strr)