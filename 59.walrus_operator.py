#walrus operator is a new addition to python 3.8 and allows us to assign as value
#some example
rahul="true"
print(rahul)
# print(rahul="false")  #it show error
#but now we use walrus operator, then
#it is detected by :=
print(rahul:="false")

#an other example using walrus operator
foods=list()
while("true"):
    food=input("enter your food")
    if food=="quite":
        break
    foods.append(food)
print(f"all foods are {foods}")

#but this is very long method so i use walrus operator
foods=list()
while (food:=input("enter your food"))!="quite":
    foods.append(food)
print(f"all foods are {foods}")