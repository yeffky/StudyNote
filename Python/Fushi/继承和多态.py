class GeometricObject:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def ifFilled(self):
        return self.filled
    
    def setFilled(self, filled):
        self.filled = filled

    def __str__(self):
        return 'color:' + self.color + 'and filled:' + str(self.filled)
        

class Circle(GeometricObject):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def getRadius(self):
        return self.radius
    
