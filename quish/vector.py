import typing

import numpy

Numerical = typing.Union[int, float]


class Vector:
    x: float
    y: float

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.x = float(kwargs.pop("x", 0))
            self.y = float(kwargs.pop("y", 0))
        elif len(args) == 0:
            self.x = 0.0
            self.y = 0.0
        elif len(args) == 1 and isinstance(args[0], Numerical):
            self.x = float(args[0])
            self.y = float(args[0])
        elif len(args) == 1:
            self.x = float(args[0][0])
            self.y = float(args[0][1])
        elif (
            len(args) == 2
            and isinstance(args[0], Numerical)
            and isinstance(args[1], Numerical)
        ):
            self.x = float(args[0])
            self.y = float(args[1])
        else:
            raise TypeError(
                "Vector() takes 0~2 positional arguments or and 2 keyword arguments x and y"
            )

    def __add__(self, other):
        other = Vector(other)
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        other = Vector(other)
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        other = Vector(other)
        return self.__class__(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        other = Vector(other)
        try:
            return self.__class__(self.x / other.x, self.y / other.y)
        except ZeroDivisionError:
            return self.__class__(0, 0)

    def __pow__(self, power, modulo=None):
        power = self.__class__(power)
        return self.__class__(self.x**power.x, self.y**power.y)

    def __pos__(self):
        return self.__class__(self.x, self.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __iadd__(self, other):
        other = self.__class__(other)
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        other = self.__class__(other)
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        other = self.__class__(other)
        self.x *= other.x
        self.y *= other.y
        return self

    def __idiv__(self, other):
        other = self.__class__(other)
        self.x /= other.x
        self.y /= other.y
        return self

    def __ipow__(self, other):
        other = self.__class__(other)
        self.x **= other.x
        self.y **= other.y
        return self

    def __abs__(self):
        return self.__class__(abs(self.x), abs(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __len__(self):
        return 2

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"{self.__class__}({self.x}, {self.y})"

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == "x":
            return self.x
        elif item == "y":
            return self.y
        else:
            raise KeyError("Vector index must be 0, 1, 'x', or 'y'")

    def dot(self, other):
        other = Vector(other)
        return self.x * other.x + self.y * other.y

    @property
    def length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def distance(self, other):
        delta = self - Vector(other)
        return delta.length

    @property
    def norm(self):
        return self / self.length
