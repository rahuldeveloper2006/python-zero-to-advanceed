#raising custom error means error can generate by user i.e manually
a=int(input("enter a number between 5 to 9"))
if(a<5 or a>9):
    raise ValueError("value error is generate so please enter value between 5 to 9")
