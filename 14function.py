#function is a block of statements which perform specified tasks whenever it is called
#there having two types of function
#1.built in function, 2. usre defined function
#built in function means the function already define (predefine) in python
#user define function means the function which is defined by user
# its syntax is:-
#def function_name(parameters):
     #statements
def sum(a,b):
    print("its addition is",a+b)
def sub(a,b):
    print("its substraction is",a-b)
def mul(a,b):
    print("its multiplication is :",a*b)
def div(a,b):
    print("its devision is:",a/b)
a=float(input("enter your 1st number"))
b=float(input("enter your 2nd number"))
sum(a,b)
sub(a,b)
mul(a,b)
div(a,b)
