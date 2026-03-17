def compare(a,b):
    '''here the function take two parameters and then compare it greater or smaller'''
    if(a>b):
        print(a,"is greater than",b)
    elif(a==b):
        print("both are equal to each other")
    else:
        print(b,"is greater than ",a)

compare(2,5)
print(compare.__doc__) #here print description of function, called docstrings
#------------------------------- -------------- ------  ----    ----    ----------- --------    ---------   -------)
def name(a):
    """here the function take name and print it"""
    print(a)
name('rahul')
print(name.__doc__)

