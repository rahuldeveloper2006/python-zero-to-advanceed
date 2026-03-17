#hybrid inheritance is a types of a ineritance it is a combination of single and multiple inheritance
#some example:-
class vehicle:
    def __init__(self,name):
        self.name=name
    def statement1(self):
        print(f"the name of vehicle is {self.name}")
class car(vehicle):
    def __init__(self,name,colour):
        vehicle.__init__(self,name)
        self.colour=colour
    def statement2(self):
        vehicle.statement1(self)
        print(f"the colour the car is {self.colour}")
class bus(vehicle):
    def __init__(self,wheel_number):
        self.wheel_number=wheel_number
    def statement3(self):
        car.statement2(self)
        print(f"the number of wheel of bus is {self.wheel_number}")
class combination(car,bus):
    def __init__(self,name,colour,wheel_number):
        bus.__init__(self,wheel_number)
        car.__init__(self,name,colour)
    def statement4(self):
        bus.statement3(self)
o=combination("car","black","6")
o.statement4()