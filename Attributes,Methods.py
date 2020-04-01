 #Creating a super class called Shapes.This is an abstract class
class Shapes:
    pass
# Creating subclass called Circle inheriting from Shapes. See Shapes is in brackets to indicate inheritance
class Circle(Shapes):
# This is a constructor which is used to intialise fields (variables)
    def get_Radius(self):
            Answer = self.Radius
            return Answer

    def get_Area(self):
        Answer1 =(self.length * self.width)
        return Answer1

#This is a method to calculate Perimeter
    def get_Perimeter(self):
        Answer2 = (self.pi * self.Radius * 2)
        return Answer2

#This is a method to calculate area
    def getradius1(self):
        answer = self.radius1 * self.radius1
        return answer
#radius1 is a field or variable
Radius1 = int(input("Please enter the radius of a circle:\n"))
#objCircle is the object from the class Circle
objCircle = Circle(radius)
#Printing my results & call the method getArea1 using the object
print("perimeter of a circle is", objCircle.getradius1, "cm2")

