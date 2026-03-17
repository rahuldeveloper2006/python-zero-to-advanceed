#list,tuples store more than one data using more location but
#but generator it store data constituents without uising memory location
#some example:-
def my_generators():
    for i in range(5):
        yield i
gen=my_generators()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def our_generator():
    for i in range(4000):
        yield i
generation=our_generator()
for j in generation:
    print(j)