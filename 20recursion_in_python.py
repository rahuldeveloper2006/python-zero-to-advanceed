#NOW WE STUDY IN RECURSION IN PYTHON
#NORMALLY RECURSION MEANS A FUNCTION CAll to ITSELF
#now we write a programe find factorial of N
#we write a programe by using recursion function 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
#write a programe to print fibonacci sequence

#we can make a programe to find factorial of number without using recursion
class person:
    '''rahul is a good boy'''
    print("rahul")
a=person()
print(a.__doc__)

def factoriall(w):
    count=1
    if(w==0 and w==1):
        return 1
    elif(w<0):
        return 0
    else:
        while(w>=1):
            count=count*w
            w=w-1
        print(count)

factoriall(w=5)