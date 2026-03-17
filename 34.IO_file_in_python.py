#io file means we can read , write ,append on a file
#if we can read a file then 
# f=open('rahul.txt','r')
# rahul=f.read()
# print(rahul) 

#if we want write some in file then
# e=open('rahul.txt','w')
# writ=e.write("hello my all friend \n always stay happy \n and take care yourself")
# print(writ) #here new writing sentence entered but previous data all removed
# e.close()

# e=open('rahul.txt','a')
# apend=e.write("my mom is my heart")
# print(apend)
# e.close()

# f=open('rahul.txt','r')
# raed=f.read()
# print(raed) #here all writing data and append data we can read
# f.close()

#we can also open and read without close by using "with statement" 
# with open('rahul.txt','a') as f:
#     f.write("my papa is my brave")
    
#now we use read lines method
# with open('rahul.txt','r') as f:
#     while 'true':
#      line1=f.readline()
#      print(line1)
#      if not line1:
#        break
     

with open("store.txt","r") as f:
    line1=f.readline()
    print(line1)