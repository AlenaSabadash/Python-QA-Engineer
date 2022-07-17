from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, name: str, side1: float, side2: float):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self) -> float:
        return self.side1 * self.side2

    @property
    def perimeter(self) -> float:
        return 2 * (self.side1 + self.side2)
