import pytest
from isTriangle import Triangle

def test_negative_or_zero_inputs():
    # Covers if a <= 0, b <= 0, c <= 0 conditions
    assert Triangle.classify(0, 1, 2) == Triangle.Type.INVALID
    assert Triangle.classify(1, 0, 2) == Triangle.Type.INVALID
    assert Triangle.classify(1, 2, 0) == Triangle.Type.INVALID
    assert Triangle.classify(-1, 2, 3) == Triangle.Type.INVALID

def test_trian_variable_paths():
    # Covers trian == 0, == 1, == 2, == 3, > 3
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE      # trian = 0
    assert Triangle.classify(3, 3, 5) == Triangle.Type.ISOSCELES    # trian = 1
    assert Triangle.classify(3, 5, 3) == Triangle.Type.ISOSCELES    # trian = 2
    assert Triangle.classify(5, 3, 3) == Triangle.Type.ISOSCELES    # trian = 3
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL  # trian > 3

def test_triangle_inequality_failures():
    # Covers cases where triangle inequality fails (a + b <= c, etc.)
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID
    assert Triangle.classify(2, 3, 5) == Triangle.Type.INVALID
    assert Triangle.classify(5, 1, 1) == Triangle.Type.INVALID

def test_isosceles_but_invalid():
    # Test ISOSCELES conditions with invalid triangle inequality
    assert Triangle.classify(5, 5, 10) == Triangle.Type.INVALID
    assert Triangle.classify(10, 5, 5) == Triangle.Type.INVALID
    assert Triangle.classify(5, 10, 5) == Triangle.Type.INVALID

def test_floating_point_and_large_valid():
    # Floating-point and large valid triangle
    assert Triangle.classify(3.5, 3.5, 3.5) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(1.1, 1.1, 1.5) == Triangle.Type.ISOSCELES
    assert Triangle.classify(1000, 1001, 1002) == Triangle.Type.SCALENE

if __name__ == "__main__":
    pytest.main()
