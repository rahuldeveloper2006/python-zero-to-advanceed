# a=float(input("enter your 1st number"))
# char=input('enter your operation')
# b=float(input("ente your 2nd number"))
# match char:
#     case '+':
#         print(b+a)
#     case '-':
#         print(a-b)
#     case '*':
#         print(b*a)
#     case '/':
#         print(a/b)
#     case _:
#         print(a%b)

        
a=int(input("enter 1st number"))
d=int(input("enter 1 for addition\n enter 2 for subtraction\n enter 3 for multiplication\n enter 4 for division"))
b=int(input("enter 2nd number"))
match d:
    case 1:
        print("the sum of",a,"+",b,"is =",a+b)
    case 2:
        print("subtraction=",a-b)
    case 3:
        print("multiplication=",a*b)
    case 4:
        print("division=",a/b)
    case _:
        print("reminder is=",a%b)