#map function
list1=[1,2,3,4,5,6,7,8]
def mul(a):
    return a*a 
# list2=[]
# for i in list1:
#     print(list2.append(i*i)
# print(list2)

#but we print same list with shortcut method by using map function
# newlist=list(map(mul,list1))
# print(newlist) #here same print the listr takeplace

# #and other method by using map and lambda function
# newlist=list(map(lambda x:x*x,list1))
# print(newlist)

# newlist=list(map(lambda x:x>3,list1))
# print(newlist)     #it print true if x>3 other wise print false


# #filter function:-
# def greater(y):
#     return y>2
# newlist1=list(filter(greater,list1))
# print(newlist1) #here print that number which num>2 otherwise skip the number

# newlist=list(filter(lambda x:x>2,list1)) #also we can use 
# print(newlist)   #here all numbers print which x>2 ,otherwise skip the number

newlist=list(filter(lambda x:x<4,list1))
print(newlist)

#reduce function:-
#reduce function take two arguments
# from functools import reduce
# newlist2=reduce(lambda x,y:x*y,list1)
# print(newlist2) #here print sum of all numbers in a list

