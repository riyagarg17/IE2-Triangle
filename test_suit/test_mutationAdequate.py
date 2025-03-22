import pytest
from isTriangle import Triangle

def test_equilateral():
    # trian > 3
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL

def test_scalene():
    # trian == 0; passes triangle inequality
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE

def test_invalid_negative_and_zero_sides():
    assert Triangle.classify(-1, 2, 3) == Triangle.Type.INVALID
    assert Triangle.classify(0, 4, 5) == Triangle.Type.INVALID
    assert Triangle.classify(5, 0, 3) == Triangle.Type.INVALID
    assert Triangle.classify(4, 5, 0) == Triangle.Type.INVALID

def test_invalid_triangle_inequality():
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID
    assert Triangle.classify(3, 1, 2) == Triangle.Type.INVALID
    assert Triangle.classify(2, 3, 5) == Triangle.Type.INVALID
    assert Triangle.classify(10, 1, 1) == Triangle.Type.INVALID

def test_isosceles_all_paths():
    # trian == 1 and a + b > c
    assert Triangle.classify(3, 3, 4) == Triangle.Type.ISOSCELES
    # trian == 2 and a + c > b
    assert Triangle.classify(4, 5, 4) == Triangle.Type.ISOSCELES
    # trian == 3 and b + c > a
    assert Triangle.classify(5, 4, 4) == Triangle.Type.ISOSCELES

def test_isosceles_but_invalid():
    # trian == 1, but a + b <= c
    assert Triangle.classify(1, 1, 2) == Triangle.Type.INVALID
    # trian == 2, but a + c <= b
    assert Triangle.classify(1, 3, 1) == Triangle.Type.INVALID
    # trian == 3, but b + c <= a
    assert Triangle.classify(4, 2, 2) == Triangle.Type.INVALID

def test_floating_point_precision():
    assert Triangle.classify(3.5, 3.5, 3.5) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(2.0, 2.0, 3.9) == Triangle.Type.ISOSCELES
    assert Triangle.classify(2.1, 3.2, 4.5) == Triangle.Type.SCALENE

def test_large_numbers():
    assert Triangle.classify(10000, 10000, 10000) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(100000, 100001, 100002) == Triangle.Type.SCALENE

if __name__ == "__main__":
    pytest.main()
