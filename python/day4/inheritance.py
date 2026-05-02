class Vechile:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed


class Car(Vechile):
     def describe(self):
         return f"this is car brand of {self.brand} nand has speed of {self.speed}"



class bike(Vechile):
     def describe(self):
         return f"this is bike brand of {self.brand} nand has speed of {self.speed}"



b=bike('hero',100)
print(b.describe())

c=Car('bmw',200)
print(c.describe())



'''

2nd question

'''

class animal:
    def who(self):
        return f"Hi i am in animal"


class mamal(animal):
    def why(self):
        return f"am in animal"


class dog(mamal):
    def what(self):
        return f"am in in mamal"


d=dog()
print(d.what())
print(d.why())
print(d.who())

'''
3
'''

class a:

    def show(self):
        print("hi i am in a")
    

    
class b(a):
    def show(self):
        super().show()
        print( f"hi i am in b")
    


out=b()
out.show()