# import math

# class circle:
#     def __init__(self, radius):
#         # 私有变量
#         self.__radius = radius
#     def getArea(self):
#         return math.pow(self.radius, 2) * math.pi
#     def getPerimeter(self):
#         return 2 * math.pi * self.radius
#     def setRadius(self, radius):
#         self.__radius = radius
#     def getRadius(self):
#         return self.__radius

# if __name__ == '__main__':
#     c = circle(5)
#     # print(c.getArea(), c.getPerimeter())
#     print(c.getRadius())

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def breath(self):
#         print("breath")

# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def breath(self):
#         print("use mouth")
    
#     def bark(self):
#         print("bark")

# if __name__ == '__main__':
#     dog = Dog('xiaobai', 16)
#     animal = Animal('xiaohei')
#     animal.breath()
#     dog.breath()
#     dog.bark()