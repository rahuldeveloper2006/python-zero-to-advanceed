#decorators are powerfull and versatile tool that allow you to modify the behaviour and method of a functions
#decorators are a function it take another function as a argument and give a new function
#two types of decorator are available
# 1. default decorator and 2. parameterized decorator
# now we study default decorator
# def greet(fx):
#    def mfx():
#       print("good morning user")
#       fx()
#       print("thank you so much user for use me")
#    return mfx

# @greet
# def welcome():
#    print("hello rahul")
# welcome()
# #and other method which is we call the function without use @greet
# greet(welcome)()

# @greet
# def add(x,y):
#    print(x+y)
# add(12,23)

#now we parameterized decorator
def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using function")
    return mfx

# @greet
# def add(a,b):
#     print(a+b)

# add(12,45)

@greet
def hello():
    print("hello iam a rahul iam from sidhakhandi")

hello()