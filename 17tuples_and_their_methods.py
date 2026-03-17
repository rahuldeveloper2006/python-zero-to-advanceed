#tuples is built in datatype
#it is immutable sequence of values
#list is mutable but tuples is immutable
#its syntax is , tup=(data,data,data)
#it can store mpore than one data with different datatype 
rahul=(1,'w',2,7.9)
print(rahul)
print(type(rahul))
print(len(rahul))
print(rahul[1])
#tuples slicing like as str slicing
print(rahul[1:3])
#now we print in the form of negative index
print(rahul[-4:-1])
#tup[2]=23 is not allowed in python
#list[2]=23 , is allowed in python
#tuples methods are
#tup.count(el) means it print the repeation of elements
tup=('a','b','a','c','a','e')
print(tup.count('a'))
#we cannopt change the tuple further 
#but we can change the tuple by convert to list
fav6=("puja","kiran","lopa","jyoti","pragyan")
print(fav6,"but one is absent so we add")
friends=list(fav6)
friends.append("gudu")
friends[2]="rahul"
print(friends)
print("but rahul is external part so")
friends.pop(2)
friends.append("lopa")
fav6=tuple(friends)
print("finally fav six is",fav6)
