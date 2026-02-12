class InvalidRadiusException(RuntimeError):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

class GeometricObject:
    def __init__(self, color, filled):
        self.__color = color
        self.__filled = filled

    def __init__(self) -> None:
        pass

    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color

    def ifFilled(self):
        return self.__filled
    
    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return 'color:' + self.__color + 'and filled:' + str(self.__filled)
        

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.setRadius(radius)

    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise InvalidRadiusException(radius)
    
if __name__ == '__main__':
    try:
        c1 = Circle(1)
        c2 = Circle(-1)
    except InvalidRadiusException as ex:
        print('Radius ' + str(ex.radius) + ' is not valid radius')