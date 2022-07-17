from src.figure import Figure


class Square(Figure):
    def __init__(self, name: str, side: float):
        super().__init__(name)
        self.side = side

    @property
    def area(self) -> float:
        return self.side**2

    @property
    def perimeter(self) -> float:
        return 4 * self.side
