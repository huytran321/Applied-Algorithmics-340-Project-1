#Huy Tran
#10/2/19
#Goal: Create a system that sets a point and gives it a radius to make a circle 
#Default Ciricle is (0, 0, 1)
import math
class Circle:
    def __init__(self, x = 0, y = 0, r = 0):
        if  r > 0:
            self.__x = x
            self.__y = y
            self.__r = r
        else:
            self.__x = x
            self.__y = y
            self.__r = 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__r

    def setX(self, x = 0):
        if x >= 0:
            self.__x = x
        else:
            self.__x = 0

    def setY(self, y = 0):
        if y >= 0:
            self.__y = y
        else:
            self.__y = 0

    def setRadius(self, r = 1):
        if r >= 0:
            self.__r = r
        else:
            self.__r = 0

    def getArea(self):
        return self.__r **2 * math.pi

    def getPerimeter(self):
        return self.__r * 2 * math.pi

    def isPointWithinCircle(self, x, y):
        if (x - self.__x) ** 2 + (y - self.__y)** 2 <= self.__r ** 2:
            return True
        else:
            return False

 