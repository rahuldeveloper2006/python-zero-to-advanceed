#list is a builtin datatype
#list means it can store the set of values with different datatype
# its syntax is, list=[int,float,char]
# ex
list=['rahul',23,23.45,'ritik','rohon'] 
print(list)
print(type(list))
print(len(list))
print(list[1])
#we canot change the value of string further i.e immutable
#but in case of list we can change the value further mutable
#some ex:-
list[3]='pakruti'
print(list)
#now we study list slycing 
# #list slycing is same as string slycing
list1=[23,23.56,24,'RAHUL','ROHON']
print(list1[0:4])
#now we study jumping index
list9=[i for i in range(23) ]
print(list9)
print(list9[1:20:2])# it print 1 to 19 then jump by 2 step
#we also use condition in list
list7=[i*i for i in range(20) if(i%2==0)]
print(list7)
#now we study diferent types of list methods
#method-1
#list.append() means it add the value at the end
print(list1.append(34))
print(list1)
#method=2
#list.sort() means it print the value in ascending order
list2=[12,45.46,87,877,4]
print(list2.sort())
print(list2)
#list.sort(reverse=true) means it print in descending order
print(list2.sort(reverse='true'))
print(list2)
#list.reverse( ) means it print the given data in reverse order
print(list2.reverse())
print(list2)
#list.remove(desire value) means it remove the desire value
print(list2.remove(12))
print(list2)
#list.pop(idx)means it remove the value of idx
print(list2.pop(2))
print(list2)
#list.insert(idx,element) means it insert the value at their given idx
print(list2.insert(2,34)) 
print(list2)

str="rahul hrll etr lki dgry ghsdjh"
words=[word.capitalize() for word in str.split()]
print(words)
list10=[12,34,56]
print(list10.extend("rahul")) 
print(list10) #extend only take string not the integer
list10.append("rohon")
list10.append(10)
list10.extend("puja") #extend method only take string value and split the string in to char
print(list10)
