from src.figure import Figure


class Triangle(Figure):
    def __init__(self, name: str, side1: float, side2: float, side3: float):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    @property
    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3
