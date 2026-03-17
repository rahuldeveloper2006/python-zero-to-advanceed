#wap to input user's first name and print its length
str1=input("enter user's name")
print(len(str1))
#2> wap to find the occurance s in a string
str2=input("enter in your about")
print(str2.count('s'))
str3='rahul'
print(str3)
print(str3.replace("rahul","puja"))
# wap to ask the user to enter names of their 5 favourite friends and store in list
str=[]
str1=input("enter your 1st friend")
str2=input("enter your second friend")
str3=input("enter your third friend")
str4=input("enter your fourth friend")
str5=input("enter your fifth friend ")
str.append(str1)
str.append(str2)
str.append(str3)
str.append(str4)
str.append(str5)
print(str)
#shortcut method for print 5 friends in a list
str6=[]
str6.append(input("enter your 1st friend"))
str6.append(input("enter your 2nd friend"))
str6.append(input("enter your third friend"))
str6.append(input("enter your 4th friend"))
str6.append(input("enter your 5th friend"))
print(str6)
#very shortcut method for print 5 friends
strr1=[]
for i in range(1,7):
    strr1.append(input("enter your friends name"))
print(strr1)
# wap to check it , if a list contains a palindrum number of elements
list=[1,2,3,2,1]
list2=list.copy()
list2=list2.reverse()
if(list==list2):
    print("the list contain palindrum number")
else:
    print("list not contain palindrum number")
# wap to count the number of students with the a grade in the following tuple
tup=('a','b','c','a','a','a')
print(tup.count('a'))