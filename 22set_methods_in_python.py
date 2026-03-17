#now we study different types of set method
set1={1,2,3,4,5,6,7}
set2={8,9,10,3,5,6,7,2}
print(set1.union(set2)) #here print the all items
print(set1.intersection(set2))# here print the common items 
print(set1.add('RAHUL'))# here rahul add in set1
print(set1)
print(set2.add('ritik'))# here add ritik in set2
print(set2)
print(set1.remove(5)) # here remove the 5 in set1
print(set1)
print(set2.clear()) #here clear the all items in set
print(set2)
print(set1.pop()) #remove a item randomly
print(set1)
set3={1,2,3,4,5,6}
set4={7,8,9,10,11,4,5,6,7,3}
set3.symmetric_difference(set4) #here using logic is= A del B (A union B)-(A intersection B)
print(set3)
set3.difference(set4) #here vusing logic is:- A-B
print(set3)
set4.difference(set3) # here using logic is :- B-A
print(set4)
set3.issuperset(set4) #her set3 is the super set of set4
print(set3)
set4.issuperset(set3) #here set4 is super set of set3
print(set4)
print(set3.isdisjoint(set4))
set3.update(set4) # set3 is get update i.e the values of set4 add in set3
print(set3)
set3.issubset(set4) #here the set3 is the subset of set4
print(set3)
set3.discard(4) # here remove the 4 in set3
print(set3)
del set4 # means here the set4 permanetely delet

