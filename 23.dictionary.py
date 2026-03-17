#dectionary is a set of unordered data items, it can store more data unorderly
#dictionary is mutable. it can change for further uses. but it cannot store duplicate value
student={
    "name":"rahul kumar bhuyan",
    "subject":["mil","math","history"],
    "age":18,
}
print(student) # it can print all key with their values
print(student["name"]) # it print value of key i.e rahul kumar bhuyan
print(len(student))
print(type(student))
name={} #its type is null dictionary
print(type(name))
#now we write a programe to print registration number of students
registration={
    144:"rahul kumar bhuyan",
    141:"puja maharana",
    142:"purna chandra",
    145:"pragyan priyadarshani",
}
print(registration[int(input("enter your regd number"))])

about={
    "name":"rahul kumar bhuyan",
    "age":18,
    "class":"btech",
    "branch":"cse",
}
#now we print all key values
#by using string format method
print(about.__format__)
#we also print by using f string
for i in about.keys():
    print(f"the value corresponding to the key {i} is {about[i]}")

#now we print all keys of dictionary
print(about.keys())
#now we print all values of dectionary
print(about.values())
