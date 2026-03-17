#lambda is also a built-in function , it helps to define a function in one line instead of multi line
#some example:-
# def sum(a,b):
#     print(a+b)

# sum(12,12) # it print 24
#but in case of lambda function work same as upper function
# sum=lambda x,y : x+y
# print(sum(12,12)) #it print 24 same as upper function
# #lambda function is very useful for make short a programe
multi=lambda x: x*x
print(multi(2)) #it print 4

#we also call a function in other function
def sum(fx,value):
    return 6+fx(value)
print(sum(lambda x : x*x,4))
