#!/usr/bin/python3

"""class Rectangle that implements Base."""

from models.base import Base


class Rectangle(Base):
    """
    Subclass of class Base
    class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instances for class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # Calling the super class

    @property
    def width(self):
        """getter for __width
            Returns: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width.
            Args:
                value (int): value to be set."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height
            Returns: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height
            Args:
                value (int): value to be set"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x.
            Returns: x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x.
            Args:
                value (int): value to be set."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y
            Returns: y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y
            Args:
                value (int): value to be set."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the class Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the class Rectangle instance with '#'"""
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__width + self.__x):
                if n < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """"overriding __str__()"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"assigns an argument to each attribute"""

        up = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, up[i], args[i])

        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """Returns dict representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            'width': self.__width,
        }
