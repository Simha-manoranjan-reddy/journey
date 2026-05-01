class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def cardetails(self):
        return f"car brand is {self.brand} and its speed is {self.speed}"
    

c = car('bmw',123)

print(c.cardetails())