#slicing
#slicing means:- we can access a part of string
# its syntax is :- str[starting index: ending index].
#starting index include but ending index not include
#some ex:-
str="rahul kumar bhuyan"
print(str[1:6])#starting from 1 and ending with 5
print(str[ :7])#starting from 0 end with 6
print(str[0:])#it starting from 0 to str(len) i.e print completely name
#negative index:-
#A   P   P  L  E
#-5  -4 -3 -2 -1
str1='apple'
print(str1[-5:-1])#starting from -5 end with -2
#list slicing
list=['rahul','rohon',23,23.67]
print(list[0:3])