#break statement is used to break the loop and a statement
#some example
for i in range(15):
    print(i,sep="~")
    if(i==10):
        print("break the loop")
        break


#now we study continue statement
#continue statement means it continue the itteration of loop
for i in range(15):
    if(i==10):
        print("continue the loop")
        continue
    print(i,end=" ")

for i in range(15):
    if(i==10):
        continue
    print(i,end=" ")
