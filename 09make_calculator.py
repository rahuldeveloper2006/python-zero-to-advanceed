print("welcome to my calculator")
a=float(input("enter your 1st number"))
print("1 for addition\n 2 for sub\n 3 fot mul\n4 for div")
b=int(input("enter your operation"))
c=float(input("enter your 2nd number"))
if(b==1):
    print(a+c)
elif(b==2):
    print(a-c)
elif(b==3):
    print(a*c)
else:
    print(a/c)

#an other types of calculator
print("welcome to our new version calculator") 
x=float(input("enter your 1st number"))
char=input('enter your operaton')
y=float(input("enter your 2nd number"))
match char:
    case '+':
        print(x+y)
    case '-':
        print(x-y)
    case '*':
        print(x*y)
    case '/':
        print(x/y)
    case _:
        print(x%y)
        