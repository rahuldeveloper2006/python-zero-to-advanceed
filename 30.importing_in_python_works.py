#importing in python is the process of loading code from python module in the current function
#for ex:-
# import math
# result=math.sqrt(4)# here math is the module and squart is a function of module math
# print(result)

# from math import sqrt,pi
# result=sqrt(9)
# print(result) # here both pi and sqrt functions loading from math module

#now we import every functions and variables in a module , we use *
#star* can help us to acess every functions and variables from amodule
#for ex:-
from math import *
result=sqrt(9)
print(result)
result2=pi
print(result2)
print(dir("math"))

#now we use "as" for give other name
# import math as m
# result=m.sqrt(34)
# print(result)

# from math import sqrt as s,pi as p
# result=s(34)
# result1=p
# print(result,"and",result1)

#now we use dir( ) function
#dir( ) is used to see all variables and functions froma module
# import math
# print(dir(math)) #here show all functions and variables of math module



# now we create my own file and import that file
# from rahulkumar import welcome,slogan,code
# # result=r.sum(12,12)
# # print(result)
# print(slogan)
# print(code)
# welcome()

