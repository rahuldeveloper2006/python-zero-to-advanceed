#string formating can be done in python by using format method
letter="hey my name is {} i am from {} and iam {}"
name="rahul"
country="india"
chare="ugly"
print(letter.format(name,country,chare))
letter="hey my name is {1} i am from {0} and iam {2}"
print(letter.format(country, name,chare))

#now we study f-string in python
name=input("enter your brother's name")
classs=input("enter your brother's class")
print(f"my brother name is {name} he is in class {classs}")
print(f"{2*3}")
print(type(f"{2*3}"))
