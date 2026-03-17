#method over writtinf
class rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
            return self.x*self.y
class circle(rectangle):
    def __init__(self,radius):
          self.radius=radius
          super().__init__(radius,radius)
    def circlearea(self):
               return 3.14* super().area()

a=rectangle(12,12)
print(a.area())
b=circle(5)
print(b.circlearea())
