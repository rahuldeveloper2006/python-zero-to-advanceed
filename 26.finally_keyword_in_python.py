#finally keyword is useed to exicute the code in any situation
#it always exicute even error generate
#some example
# try:
#    name=input("enter your name")
#    regdno=int(input("enter your regd number"))
#    print(f"my name is {name} and my regd number is {regdno}")
# except ValueError:
#    print("value error is generated so please enter integer regd number")
# finally:
#    print("programe is done with sucessfully") #here error is generate but finally block sucessfully start to run

#but in case of function defination there finally clause make dominant position 
def aligibility():
   try:
    n=int(input("enter your AGE"))
    if(n<18):
      print("NOT ALIGBLE")
      return 0
    elif(n>=18 and n<60):
      print("aligble")
      return 00
   except ValueError:
     print("value error is generate")
     return 1
     print("rahul") # here rahul is bydefault not printed
     #but we here we use finally keyword
   finally:
     print("the programe successfully runed") 
   
x=aligibility()
print(x)