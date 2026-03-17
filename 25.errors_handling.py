#we can also handling different types of error i.e called exception handling
#exception handling we can do by using "try" and "except" block
#some example
list=["kurkure","cooldrinks","chocolate","micture","sweets"]
try:
    ind=int(input("enter index"))
    print(list[ind])
    print(10/0)
except IndexError:
    print("error is generated please enter right index")
except ValueError:
    print("please enter integer value ")
except ZeroDivisionError:
    print("please not divide zero by any number")
print("rahul")

        