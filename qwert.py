def greet(fx):
    def mfx():
        print("good morning user")
        fx()
        print("thank you user")
    return mfx
def welcome():
    print("hello rahul")
greet(welcome)()