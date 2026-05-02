class shape:

    def __init__(self):
        pass

    def area(self):
        pass

class circle(shape):

    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        print(3.14*self.radius*self.radius
              )
        
class rectangle(shape):

    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        print(self.l*self.b
              )
        

def main():

    r=rectangle(10,20)
    r.area()

    c=circle(3)
    c.area()


if __name__== "__main__":

    main()


'''
2
'''

