from math import sqrt


class Point:
    """This class defines a point in a 2D representation and take 2 atribute
    x and y to define it

    Attribute:
        x: float

        y: float
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lower_left, upper_right):
        """Method checks if the point falls in a rectangle, takes 2 arguments
        and returns True if the point is in rectangle or False if otherwise

        Argument:
            lower_left: tuple

            upper_right: tuple
        """
        if lower_left[0] < self.x < upper_right[0] and lower_left[1] < self.y < upper_right[1]:
            return True
        return False

    def calculate_distance_to(self, other):
        """Calculates the distance between 2 points and takes 1 argument

        Argument:
            other: obj

            The second point
        """
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


p1 = Point(1, 5)
p2 = Point(5, 2)

print(p1.falls_in_rectangle((2, 4), (4, 6)))
print(p1.calculate_distance_to(p2))
