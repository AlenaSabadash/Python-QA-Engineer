from __future__ import annotations


class Figure:
    def __init__(self, name: str):
        self.name = name

    @property
    def area(self) -> float:
        raise NotImplementedError

    @property
    def perimeter(self) -> float:
        raise NotImplementedError

    def add_area(self, figure: Figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError("Метод add_area принимает только объекты с типом Figure")
        return sum([self.area, figure.area])
