import pytest

from typing import Tuple

from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (10, (100, 40)),
        (2, (4, 8)),
    ],
)
def test_square(test_input: float, expected: Tuple[float]):
    s = Square("Квадрат", test_input)
    expected_area = expected[0]
    expected_perimeter = expected[1]

    assert round(s.area, 2) == expected_area
    assert round(s.perimeter, 2) == expected_perimeter


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((5, 10, 7), (16.25, 22)),
        ((10, 10, 10), (43.3, 30)),
    ],
)
def test_triangle(test_input: Tuple[float], expected: Tuple[float]):
    t = Triangle("Треугольник", *test_input)
    expected_area = expected[0]
    expected_perimeter = expected[1]

    assert round(t.area, 2) == expected_area
    assert round(t.perimeter, 2) == expected_perimeter


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((5, 7), (35, 24)),
        ((10, 10), (100, 40)),
    ],
)
def test_rectangle(test_input: Tuple[float], expected: Tuple[float]):
    r = Rectangle("Прямоугольник", *test_input)
    expected_area = expected[0]
    expected_perimeter = expected[1]

    assert round(r.area, 2) == expected_area
    assert round(r.perimeter, 2) == expected_perimeter


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (5, (78.54, 31.42)),
        (7, (153.94, 43.98)),
    ],
)
def test_circle(test_input: float, expected: Tuple[float]):
    c = Circle("Круг", test_input)
    expected_area = expected[0]
    expected_perimeter = expected[1]

    assert round(c.area, 2) == expected_area
    assert round(c.perimeter, 2) == expected_perimeter


@pytest.mark.parametrize(
    "figures,expected",
    [
        ((Rectangle("Прямоугольник", 5, 7), Circle("Круг", 5)), 113.54),
        ((Rectangle("Прямоугольник", 5, 7), Rectangle("Прямоугольник", 5, 7)), 70),
        ((Triangle("Треугольник", 5, 10, 7), Circle("Круг", 5)), 94.79),
    ],
)
def test_add_area(figures: Tuple[Figure], expected: float):
    f1 = figures[0]
    f2 = figures[1]
    assert round(f1.add_area(f2), 2) == expected


@pytest.mark.parametrize(
    "figures",
    [
        (Rectangle("Прямоугольник", 5, 7), None),
        (Rectangle("Прямоугольник", 5, 7), "test_figure"),
    ],
)
def test_add_area_wrong_value(figures: Tuple[Figure]):
    """
    Проверка, что метод add_area вызывает исключение ValueError, если в параметре не передан тип Figure
    """
    f1 = figures[0]
    f2 = figures[1]

    with pytest.raises(ValueError):
        f1.add_area(f2)
