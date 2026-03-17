#now we learn different types of dictionary methods
student={
    "name":"rahu kumar bhuyan",
    "vilage":"sidhakhandi",
    "age":18,
    "clas":"btech",
    "mark":[98,89,90,100],
}
friends={
    1:"kiran",
    2:"puja",
    3:"jyoti",
    4:"pragyan",
    5:"lopa",
    6:"rahul",

}

# print(student.values()) # here print all values of dictionary
# print(student.keys()) #here print only keys in dict
# print(student.items()) #here print both keys and values
# print(student.pop("mark")) # here mark removed
# print(student)
# print(student.get("name")) # here the value of name is print
# print(student["name"])
# op=list(friends.values()) #here the all values of dict print in the form of list
# print(op)
# op=list(friends.keys()) #here the all keys os dict print in the form of list
# print(op)
# op=list(friends.items()) #here the both keys and values are printed
# print(op)
# friends=dict(op)
# print(friends)
# print(friends.get("name2"))# here name2 is absent in dictionary so it print none
friends.update(student)
print(friends)
dict={
    'a':[1,3,4,5,9],
    'b':(12,4,5,67),
}
dict2={
    "roll":132,
    "rill":234,

}
# print(dict.update(dict2)) #here all items of dict2 transfer to dict1
# print(dict)
print(dict2.fromkeys(dict2))


