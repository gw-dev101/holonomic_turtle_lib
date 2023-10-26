from turtle import *
from math import cos, sin, pi

class Holonomic_turtle(Turtle):
    """A turtle that can move in any direction it has 3 motors that can be set to any speed
    The motors are numbered 1, 2, 3 and are at 120 degrees from each other starting at 0 degrees
    The turtle has a base diameter and a wheel diameter
    the base diameter is the distance between the center of the turtle and the center of the wheels
    the wheel diameter is the diameter of the wheels it affects the speed of the turtle"""
    def __init__(self):
        Turtle.__init__(self, shape="turtle")
        self.color("blue")
        self.pensize(5)
        self.speed(0)
        self.motor1 = 0
        self.motor2 = 0
        self.motor3 = 0
        self.wheel_diameter = 0.1
        self.base_diameter = 3
        self.rotation = self.heading()
        self.goto(0, 0)
        self.pendown()
        self.wheels = []
        for i in range(3):
            self.wheels.append(Turtle(shape="circle"))
            self.wheels[i].color(["red", "green", "blue"][i])
            self.wheels[i].shapesize(self.wheel_diameter, self.wheel_diameter)  
            self.wheels[i].penup()
            self.wheels[i].pensize(2)
            self.wheels[i].goto(self.xcor() + self.base_diameter * cos(2 * pi * i / 3 + self.rotation), self.ycor() + self.base_diameter * sin(2 * pi * i / 3 + self.rotation))

    def wheels_down(self):
        for i in range(3):
            self.wheels[i].pendown()
    def wheels_up(self):
        for i in range(3):
            self.wheels[i].penup()
    def set_wheel_diameter(self, diameter):
        self.wheel_diameter = diameter
        for i in range(3):
            self.wheels[i].shapesize(self.wheel_diameter, self.wheel_diameter)
    #2 versions one for all wheels the same color and one for different colors
    def set_wheel_color(self,color,color2=None,color3=None):
        if color2 is None:
            for i in range(3):
                self.wheels[i].color(color)
        else:
            self.wheels[0].color(color)
            self.wheels[1].color(color2)
            self.wheels[2].color(color3)
    def move(self):
        x = self.xcor()
        y = self.ycor()
        radian_rotation = self.rotation * pi / 180  # Convert to radians
        x += self.motor1 * cos(radian_rotation) + self.motor2 * cos(radian_rotation + 2 * pi / 3) + self.motor3 * cos(radian_rotation + 4 * pi / 3)
        y += self.motor1 * sin(radian_rotation) + self.motor2 * sin(radian_rotation + 2 * pi / 3) + self.motor3 * sin(radian_rotation + 4 * pi / 3)
        self.goto(x, y)
        self.rotation += (self.motor1 + self.motor2 + self.motor3) / 3
        self.rotation %= 360
        self.setheading(self.rotation)
        for i in range(3):
            wheel_rotation = self.rotation + i * 120
            self.wheels[i].setheading(wheel_rotation)
            wheel_x = x + self.base_diameter * cos(wheel_rotation * pi / 180)
            wheel_y = y + self.base_diameter * sin(wheel_rotation * pi / 180)
            self.wheels[i].goto(wheel_x, wheel_y)
