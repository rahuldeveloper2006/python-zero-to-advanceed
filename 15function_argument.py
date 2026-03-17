#function argument
#there are having four types of statement
#there are default, keyword, variable, required argument
#default argument
def averg(a=12,b=24):
    print("its average is :",(a+b)/2)
averg(24) #it take bydefault b=24 and print averg=24
averg(b=12)#it takes bydefault a=12 and print averg is 12
def name(fname,mname="rahul",lname="bhuyan"):
    print("good morning",fname,mname,lname)
name("mrs","puja","maharana")
name("MR","kiran","sahu")
name("mrs","jyoti","behera")

def name(**names):
    print(type(names))
    print("hello",names["fname"],names["mname"],names["lname"])
namee=name(fname="rahul",
    mname="kumar",
    lname="bhuyan",)
from functools import reduce
def average(*value):
    print(type(value))
    sum=reduce(lambda x,y:x+y,value)
    result=sum/len(value)
    print(f"average is {result}")

average(1,2,3,4)
