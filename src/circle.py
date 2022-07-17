import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * (self.radius**2)

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
