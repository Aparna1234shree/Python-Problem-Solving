"""
OOPS using Python
*** Circle- class to find area and perimeter***
list = [10,501,22,37,100,999,87,351]
class private variable named pi=3.141
class methods - area and perimeter
"""

class Circle:
    # Class private variable pi
    __pi = 3.141

    # Constructor that takes a list as an argument
    def __init__(self, radius_list):
        self.radius_list = radius_list

    # Method to calculate the area of circles in the list
    def Area(self):
        areas = []
        for radius in self.radius_list:
            area = Circle.__pi * (radius ** 2)
            areas.append(area)
        return areas

    # Method to calculate the perimeter of circles in the list
    def Perimeter(self):
        perimeters = []
        for radius in self.radius_list:
            perimeter = 2 * Circle.__pi * radius
            perimeters.append(perimeter)
        return perimeters

""" 
*** UML diagram to covert as Python class ***
radius:double = 1.0
color :String
--------------------------------------------
Circle()
Circle(radius:double)
Circle(radius:double,color:String)
getRadius():double
setRadius(radius:double):void
getColor():String
setColor(color:String):void
toString():String
getArea():double
getCircumference():double

"""

class CircleUML:
    # Class private variable pi
    __pi = 3.141

    # Constructor without arguments
    def __init__(self, radius=0.0, color=""):
        self.radius = radius
        self.color = color

    # Method to get the radius
    def getRadius(self):
        return self.radius

    # Method to set the radius
    def setRadius(self, radius):
        self.radius = radius

    # Method to get the color
    def getColor(self):
        return self.color

    # Method to set the color
    def setColor(self, color):
        self.color = color

    # Method to return the Circle information as a string
    def toString(self):
        return f"Circle(radius={self.radius}, color={self.color})"

    # Method to calculate the area of the Circle
    def getArea(self):
        return CircleUML.__pi * (self.radius ** 2)

    # Method to calculate the circumference of the Circle
    def getCircumference(self):
        return 2 * CircleUML.__pi * self.radius


# Example usage
if __name__ == "__main__":
    # Task 1 Example
    radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
    circle = Circle(radius_list)
    print("Areas:", circle.Area())
    print("Perimeters:", circle.Perimeter())

    # Task 2 Example
    circle_uml = CircleUML(5.0, "Red")
    print(circle_uml.toString())
    print("Area:", circle_uml.getArea())
    print("Circumference:", circle_uml.getCircumference())





