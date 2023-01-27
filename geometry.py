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

    def __str__(self) -> str:
        return (f"({self.x}, {self.y})")

    def __repr__(self) -> str:
        return self.__str__()

    def falls_in_rectangle(self, rectangle):
        """Method checks if the point falls in a rectangle, takes 1 argument
        and returns True if the point is in rectangle or False if otherwise

        Argument:
            rectangle: obj
                Obj created with class Rectangle
        """
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x and \
                rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            return True
        return False

    def calculate_distance_to(self, other):
        """Calculates the distance between 2 points and takes 1 argument

        Argument:
            other: obj

            The second point
        """
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Rectangle:
    """This class defines a rectancle in a 2D representation and take 2 atribute
    lower_left point and upper_right point to define it

    Attribute:
        lower_left: obj

        upper_right: obj
    """

    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right
