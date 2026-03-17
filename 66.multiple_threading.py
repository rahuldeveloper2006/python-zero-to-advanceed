#multiple threading in python is used to download files and exicute different function with short time interval and simultaneously
#some example:-
# import time
# def function1(seconds):
#     print(f"please wait {seconds} seconds")
#     time.sleep(seconds)

# #now we determine how much time take for complete run the code
# time1=time.perf_counter()
# function1(4)
# function1(3)
# function1(2)
# function1(1)
# time2=time.perf_counter()
# #now we calculate time
# print(time2-time1)  #for complete exicution it take total time 10 minutes
 
#when we use thresding then the same exicution take time very short time
# import time
# import threading
 
# def function1(seconds):
#     print(f"please wait {seconds} seconds")
#     time.sleep(seconds)

# #now we determine how much time take for complete run the code
# time1=time.perf_counter()
# t1=threading.Thread(target=function1,args=[4])
# t2=threading.Thread(target=function1,args=[3])
# t3=threading.Thread(target=function1,args=[2])
# t4=threading.Thread(target=function1,args=[1])
# t1.start()  #start function start the exicution in sequence it dont wait for end
# t2.start()
# t3.start()
# t4.start()
# time2=time.perf_counter()
# #now we calculate time
# print(time2-time1)  #in this case take time for completely execution is approximately 0.12 seconds

# # if we want to wait to end the function then start another function call , then 
import time
import threading
 
def function1(seconds):
    print(f"please wait {seconds} seconds")
    time.sleep(seconds)

#now we determine how much time take for complete run the code
time1=time.perf_counter()
t1=threading.Thread(target=function1,args=[4])
t2=threading.Thread(target=function1,args=[3])
t3=threading.Thread(target=function1,args=[2])
t4=threading.Thread(target=function1,args=[1])
t1.start()  #start function start the exicution in sequence it dont wait for end
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
time2=time.perf_counter()
#now we calculate time
print(time2-time1)  #in this case take time for completely execution is approximately 4 seconds

