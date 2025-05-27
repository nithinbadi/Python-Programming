'''
Object oriented programming homework assignment

1. Class called Line with methods called distance and slope. 
Parameters(a tuple) taken are coordinate 1 and coordinate 2.

2. Class called Cylinder with methods called Volume and Surface area.
Parameters taken are height with a default 1 and radius with a default 1.
'''

import math

# Class Line
class Line():

    def __init__(self,coord1,coord2):
        
        # Unpacking the coordinate tuples into the format (x,y) respectively
        self.x1,self.y1 = coord1
        self.x2,self.y2 = coord2

    def distance(self):
        '''
        Result:
            Distance = sqrt((x1-x2)^2 + (y1-y2)^2)
        '''
        return math.sqrt((self.x1-self.x2)**2 + (self.y1-self.y2)**2)
    
    def slope(self):
        '''
        Returns slope between coordinates (x1,x2) and (y1,y2) 
        using the formula m = (y2-y1)/(x2-x1)
        '''
        try:
            return (self.y2-self.y1)/(self.x2-self.x1)
        
        except ZeroDivisionError:
            print("Cannot divide by zero")
            


class Cylinder():

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        '''
        Formula =>
            Volume = pi * r^2 * h
        '''
        return self.radius**2 * Cylinder.pi * self.height
    
    def surface_area(self):
        '''
        Formula =>
            Surface Area = 2 * pi * r *(r + h)
        '''
        return 2*Cylinder.pi*self.radius * (self.radius +self.height)


li = Line((1,1),(4,5))

print('Distance between points is {}'.format(li.distance()))
print('Slope of the line is {}\n'.format(li.slope()))

cy = Cylinder()

print('Default cylinder volume is {}\n'.format(cy.volume()))
print('Default cylinder surface area is {}\n'.format(cy.surface_area()))

cy2 = Cylinder(3,4)

print('Cylinder volume is {}\n'.format(cy2.volume()))
print('Cylinder surface area is {}\n'.format(cy2.surface_area()))
