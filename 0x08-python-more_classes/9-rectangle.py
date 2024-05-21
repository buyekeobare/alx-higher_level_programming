#!/usr/bin/python3
"""Establishes a Rectangle class."""


class Rectangle:
    """Signifies a rectangle.
    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Ssymbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This initializes a new Rectangle.
        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrievet/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return Rectangle with the greater area.
        Args:
            rect1 (Rectangle): The first Rectangle.
            rect2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect1 or rect2 is not a Rectangle.
        """
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect2 must be an instance of Rectangle")
        if rect1.area() >= rect2.area():
            return (rect1)
        return (rect2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): Width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return printable representation of the Rectangle.
        Signifies rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
