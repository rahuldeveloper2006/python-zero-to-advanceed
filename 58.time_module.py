#the time module in python provides a set of functions to work with the related operation
#time.time() function it print the time in second from 1997 year
#wwe can calculate a person how much time take for done a work and also python
#some example:-
# import time
# def use_while():
#     i=0
#     while(i<40000):
#         i=i+1
#         print(i)
# def use_for():
#     for i in range(40000):
#         print(i)
# init=time.time()
# use_while()
# while_loop=(time.time()-init)
# init=time.time()
# use_for()
# for_loop=(time.time()-init)
# print(f"for loop take time is {for_loop}")
# print(f"while loop take time {while_loop}")
#_________________________________________________________________________________________________________________________________
#now we use time.sleep() function
#time.sleep() function it stop the exicution for some time
#its syntax is :- time.sleep(argument in sec)
# import time
# print("a person he is a very good .but their name is")
# sec=int(input("enter sec "))
# print(f"wait {sec} seconds")
# time.sleep(sec)
# print(f"name is rahul kumar bhuyan")
#_________________________________________________________________________________________________________________________________

# now we use time.strftime() it show the curent time ,year,month,date
# import time
# time_stamp=time.strftime('%H:%M:%S %Y-%m-%D')
# print(time_stamp)
#____________________________________________________________________________________________________________________________
import time
t=time.localtime()
time_stamp=time.strftime('%y-%m-%d %H:%M:%S',t)
print(time_stamp)