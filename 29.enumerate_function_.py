#enumerate function is a built-in function in python
#that allows us to loop over a sequence...such that list,tuples ,or string......and get index and element at the same time
#some example :-
names=["rahul","rohon","ritik","roshan","pakruti","rakesh"]
# j=0
# for i in range(len(names)):
#     if(j==3):
#         print("ritik is a good boy")
#     print(names[i])
#     print(j)
#     j=j+1

#but now we use enurment function which print both index and elements in shortcut method

# for index,name in enumerate(names):
#     if(index==3):
#         print("ritik is a good boy")
#     print(index,name)  # here the index starting from 0

#now we use start for change starting index
for index,name in enumerate(names,start=1):
    print(name,"\n",index)  #here the index starting from 1

#now we use f-string
for index,name in enumerate(names):
    print(f" {index+1} is for element {name}")