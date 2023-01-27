from geometry import Point, Rectangle
from random import randint

point1 = Point(randint(0, 9), randint(0, 9))
point2 = Point(randint(10, 19), randint(10, 19))
my_rectangle = Rectangle(point1, point2)

print("Rectangle coordinates:",
      my_rectangle.lower_left.x, ",",
      my_rectangle.lower_left.y, "and",
      my_rectangle.upper_right.x, ",",
      my_rectangle.upper_right.y)

user_input_x = int(input("Guess X: "))
user_input_y = int(input("Guess Y: "))

user_point = Point(user_input_x, user_input_y)

print("Your point was inside the rectangle:",
      user_point.falls_in_rectangle(my_rectangle))

print(f"Distance between the A{point1} and B{point2} is: ",
      my_rectangle.upper_right.calculate_distance_to(my_rectangle.lower_left))
