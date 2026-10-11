from abc import ABC, abstractmethod

from math import pi

class Objects3D(ABC):

    @abstractmethod
    def lsa(self) -> int:
        pass

    @abstractmethod
    def tsa(self) -> int:
        pass

    @abstractmethod
    def volume(self) -> int:
        pass

class Cube(Objects3D):

    def __init__(self, edge):
        super().__init__()
        self.edge=edge

    def lsa(self):
        """asdasda"""
        return 4*(self.edge**2)

    def tsa(self):
        return 6*(self.edge**2)

    def volume(self):
        return self.edge**3

class TraianglePyramid(Objects3D):

    def __init__(self, sides, height, base_width):
        super().__init__()
        self.sides=sides
        self.height=height
        self.base_width=base_width

    def lsa(self):
        return ((self.base_width*self.sides)*self.height)/2

    def tsa(self):
        return ((self.base_width/2)*self.height)+(((self.base_width*self.sides)*self.height)/2)

    def volume(self):
        (((self.base_width/2)*self.height)/3)*self.height

class Cylinder(Objects3D):

    def __init__(self, height, rad):
        super().__init__()
        self.height=height
        self.rad=rad

    def lsa(self):
        return 2*pi*self.rad*self.height

    def tsa(self):
        return pi*(self.rad**2)

    def volume(self):
        return pi*(self.rad**2)*self.height
    