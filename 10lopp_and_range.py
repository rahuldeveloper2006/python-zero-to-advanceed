#loop means frequently exicute of statement in loop body untill the given condition is true
#loop means contineously iteration of statement untill the certain condition reached
#there are two types of loop in python:-
#there are :- 1. for loop, 2. while loop
#for loop means repeat a specific block of code with known number of times
a=[1,3,45,67,89,23,12.44]
for i in a:
    print(i)
#now we study range( )
#range function returns a sequence of number,initiate from 0 to bydefault increment by 1 and bydefault stop before a specified number
for e in range(20):
    print(e)#here print 0 to 19

for f in range(20):
    print(f+1)# here print 0 to 20
for a in range(20):
    print(a-1) #here print 0 to 18

n=7
sum=0
for j in range(1,n+1):
    sum=sum+j
    print("total sum",sum)

for w in range(1,34):
    print(w) # it print 1 to 33
for t in range(1,5,2):
    print(t)
#now we study while loop
i=1
while(i<=10):
    print(i)
    i+=1
#print your 5 friends
list=[]
i=1
n=int(input("enter your number of friends" ))
while(i<=n):
    # str=input("enter your friend name")
    # list.append(str)
    # i=i+1
    list.append(input("enter your friend's name"))
    i=i+1
print("my",n,"favourite friends name are: ",list)



