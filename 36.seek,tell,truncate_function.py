#seek( )function is in built function in python ,it seek means jump aither forward or backward some byte
# with open("rahul.txt","r") as f:
#     reed=f.read()
#     print(reed)
#     seek=f.seek(10) #here the location jump forward 10bytes
#     red=f.read(17) #after seek 10 byte it print 17charecter after seek 10bytes
#     print(red)

#tell() function is a in built functi0n in python , it show the current location in a file
# with open("rahul.txt","r") as f:
#     reed=f.read()
#     print(reed)
#     seek=f.seek(10) #here the location jump forward 10bytes
#     print(f.tell()) #it print the current location in bytes
#     red=f.read(17) #after seek 10 byte it print 17charecter after seek 10bytes
#     print(red)

#truncate() is also a inbuilt function in python, it truncate means remove the latter in file after given bytes
# with open("rohon.txt","w") as f:
#    reed=f.write("hello world") 
#    print(reed)
#    trun=f.truncate(6) #means it print only 6 charecter after 6 charecter it get truncate
#    print(trun)
# with open("rohon.txt","r") as f: #now we read the rohon.txt file
#    red=f.read()
#    print(red) #it only read only 6 charecter hello, because after 6 charecter truncate takeplace




# with open("rahul.txt","w") as f:
#     f.write("hello iam rahul kumar bhuyan\n iam from sidhakhandi \n my age is 19 \n my regd no is 2401204144")

# with open("rahul.txt","r") as f:
#     readd=f.read()
#     print(readd)
#     f.seek(10)
#     ress=f.read(30)
#     print(ress)
#     print(f.tell())

with open("rahul.txt","a") as f:
    red=f.truncate(30)
    print(red)
with open("rahul.txt","r") as f:
    rid=f.read()
    print(rid)
