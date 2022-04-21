'''
Name: Nathan Swinger
Lab 4
'''

import math

class Point():
    'Class to represent a point on a cartesian plane'

    COUNT = 0
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.COUNT += 1
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setX(self, number):
        self.x = number
        return self.x

    def setY(self, number):
        'Can be used to set the y value of a point'
        self._y = number
        return self._y

    def distanceFromOrigin(self):
        'calculates the distance from a point to the origin'
        distance = self.x ** 2 + self.y ** 2
        distance = math.sqrt(distance)
        return distance

    def distanceFromPoint(self, other):
        'Calculates the distance between 2 points'
        distance = ((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)
        distance = math.sqrt(distance)
        return distance

    def __ne__(self, other):
        if self is other:
            return False
        if type(self) != type(other):
            return True
        else:
            return Point.distanceFromOrigin(self) != Point.distanceFromOrigin(other)
        
    def __eq__(self, other):
        'returns true if points are equal to each other, false otherwise'
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return Point.distanceFromOrigin(self) == Point.distanceFromOrigin(other)

    def __lt__(self, other):
        'Returns true if first point is less than other point, false otherwise'
        if self is other:
            return False
        elif type(self) != type(other):
            return False
        else:
            return Point.distanceFromOrigin(self) < Point.distanceFromOrigin(other)

    def __gt__(self, other):
        'Returns true if first point is greater than second point, false otherwise'
        if self is other:
            return False
        elif type(self) != type(other):
            return False
        else:
            return not Point.distanceFromOrigin(self) < Point.distanceFromOrigin(other)

    def __le__(self, other):
        'Returns true if first point is less than or equal to second point, false otherwise'
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return Point.distanceFromOrigin(self) <= Point.distanceFromOrigin(other)

    def __ge__(self, other):
        'Returns true if first point is greater than or equal to second point, false otherwise'
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return Point.distanceFromOrigin(self) >= Point.distanceFromOrigin(other)

def main():
    p1 = Point(3, 4)
    print(p1)
    p2 = Point(3, 0)
    print(Point.getX(p2), Point.getY(p2))
    print("The distance between", p1, "and", p2, "is", Point.distanceFromPoint(p1, p2))
    print("Testing the comparison operators in the order <, <=, >, >=, ==, and !=")
    print("p1 < p2?", p1 < p2)
    print("p1 <= p2?", p1<= p2)
    print("p1 > p2?", p1 > p2)
    print("p1 >= p2?", p1 >= p2)
    print("p1 == p2?", p1 == p2)
    print("p1 != p2?", p1 != p2, "\n")
    print("""p1 == "Hello"?""", p1 == "Hello")
    print("""p1 != "Hello"?""", p1 != "Hello", "\n")
    print("Number of point objects created is", Point.COUNT)

main()
