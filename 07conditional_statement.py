#wap to symbol of trafic light by using conditional statement
str1=input("enter colour of trafic light")
if(str1=='red'):
    print("stop the vehicle")
elif(str1=='yellow'):
    print("start the vehicle")
else:
    print("let to go the vehicle")

#wap to find eligibility for driving

#wap to convert a string tu list and change value then again convert from list to string
# at first convert from string to list
str2=input("enter a string")
lists=[word.capitalize() for word in str2.split()]
print(lists)
lists[0]=input("enter changed data")
#now we convert from list tu string
strings=" ".join(lists)
print(strings)
