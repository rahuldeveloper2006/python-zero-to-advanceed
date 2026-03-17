#global variable is types of variable which we can access both within and out side of the function body
#for example:--
b=34 #this is the global variable
def rahul():
    a=45  #this is the local variable
    print(a) #here the variable print 45
    print(b)  #here the global variable print 34

rahul()
print(b)  #here 34 is print because this is the global variable and its limitation is anywhere we can call 
# print(a) #here show error because this is the local variable and its limit is only in function not outside

# if we want to change the value of global variable in a function
c=34
def rohon():
    d=56
    global c
    c=10
    print(d)
rohon()
print(c)



