#set is the collection of unordered items
#it can store different items but it cannot change further
#list and dictionary are mutable but set and tuples are immutable
#its syntax is :- set={1,3,5,6,7,5}
#it can print once to the repeated number
# its examole:-
set={1,3,4,4,4,5,6,7,8,9,}
print(set)# here print the 4 only one times
print(len(set))
print(type(set))
#now we print all elements of set
for i in set:
    print(i)
set={j for j in range(20)}
print(set)

#now we learn empty set
# rahul=set()
# print(len(rahul))
# print(type(rahul))
# print(rahul)
rahul=set()
for i in range(6):
    rahul.add(input("enter your item"))
print(rahul)



