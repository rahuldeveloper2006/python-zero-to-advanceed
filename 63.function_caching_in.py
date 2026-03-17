#function caching is a technique for improving the performance of a programe by storing the results of a function call
#her the function call's data store, if sama function further became then it remind and print without computing
#this is useful when repeated data pass to calling function
#some example:-
import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")  #here computing and after computing print with take time 5 minutes
print(fx(6))
print("done for 6")
print(fx(10))
print("done for 10")
print(fx(20))
print("done for 20")  #here print speedely by remind the previous data 
print(fx(6))
print("done for 6")
print(fx(10))
print("done for 10")
print(fx(50))
print("here done for 50 ")  #here again print with computing because it is new data for function call
