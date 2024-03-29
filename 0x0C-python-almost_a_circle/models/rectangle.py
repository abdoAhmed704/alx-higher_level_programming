#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area"""
        return self.__height * self.__width

    def display(self):
        """desplay #"""
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        wi = self.width
        he = self.height
        x = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {wi}/{he}"
        return x

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, str(k), v)

    def to_dictionary(self):
        """to_dictionary"""
        lista = ["id", "width", "height", "x", "y"]
        dicta = {}
        for key in lista:
            dicta[key] = getattr(self, key)
        return dicta
