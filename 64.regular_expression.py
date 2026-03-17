# string="i was a good boy and my name is rahul kumar bhuyan"
# spliit=string.split()
# print(spliit)
# find=input("enter your desire string")
# for index,i in enumerate(spliit):
#     if(i==find):
#         print(f"{find} is found at index {index}")
#we can find charecter in text by using forloop and enumerate function
#but for this methdo we use more logic mind
#so we can use regular expression instead of for loop because it is a built in function
# import re
# pattern=input("enter your desire string")
# text="my name is rahul kumar bhuyan . and a Cyclone and Dyclone is start and make destroy to all things "
# match=re.search(pattern,text)
# print(match)  #here after print one occurance then it stop their execution
#but we want to see all occurance, then we use "re.finditer(pattern,text)"
import re
pattern=r"[A-Z]yclone"
text="my name is rahul kumar bhuyan . and a Cyclone and Dyclone is start and make destroy to all things "
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(type(match.span()))
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
