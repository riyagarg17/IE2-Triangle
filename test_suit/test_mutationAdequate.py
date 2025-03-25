import pytest
from isTriangle import Triangle

# --------------------------------------------
# Test: Equilateral triangle (all sides equal)
# Covers: trian > 3 condition and correct classification
# --------------------------------------------
def test_equilateral():
    # trian > 3
    result = Triangle.classify(5, 5, 5)
    assert result == Triangle.Type.EQUILATERAL

# --------------------------------------------
# Test: Scalene triangle (all sides different)
# Covers: trian == 0 and passes triangle inequality
# --------------------------------------------
def test_scalene():
    # trian == 0; passes triangle inequality
    result = Triangle.classify(3, 4, 5)
    assert result == Triangle.Type.SCALENE

# --------------------------------------------
# Test: Invalid triangles with zero or negative side lengths
# Covers: Early exit on a <= 0 or b <= 0 or c <= 0
# Also detects mutations that skip these checks
# --------------------------------------------
def test_invalid_negative_and_zero_sides():
    result1 = Triangle.classify(-1, 2, 3)
    assert result1 == Triangle.Type.INVALID

    result2 = Triangle.classify(0, 4, 5)
    assert result2 == Triangle.Type.INVALID

    result3 = Triangle.classify(5, 0, 3)
    assert result3 == Triangle.Type.INVALID

    result4 = Triangle.classify(4, 5, 0)
    assert result4 == Triangle.Type.INVALID

# --------------------------------------------
# Test: Triangles that violate the triangle inequality
# Covers: a + b <= c, a + c <= b, b + c <= a
# Kills mutants in inequality logic
# --------------------------------------------
def test_invalid_triangle_inequality():
    result1 = Triangle.classify(1, 2, 3)
    assert result1 == Triangle.Type.INVALID

    result2 = Triangle.classify(3, 1, 2)
    assert result2 == Triangle.Type.INVALID

    result3 = Triangle.classify(2, 3, 5)
    assert result3 == Triangle.Type.INVALID

    result4 = Triangle.classify(10, 1, 1)
    assert result4 == Triangle.Type.INVALID

# --------------------------------------------
# Test: Isosceles triangle via each trian value (1, 2, 3)
# Covers: trian == 1, 2, 3 and corresponding triangle inequalities
# Kills any mutation that misclassifies isosceles or skips its logic
# --------------------------------------------
def test_isosceles_all_paths():
    # trian == 1 and a + b > c
    result1 = Triangle.classify(3, 3, 4)
    assert result1 == Triangle.Type.ISOSCELES

    # trian == 2 and a + c > b
    result2 = Triangle.classify(4, 5, 4)
    assert result2 == Triangle.Type.ISOSCELES

    # trian == 3 and b + c > a
    result3 = Triangle.classify(5, 4, 4)
    assert result3 == Triangle.Type.ISOSCELES

# --------------------------------------------
# Test: Isosceles shape but fails triangle inequality
# Covers: correct fallback to INVALID instead of ISOSCELES
# Kills: incorrect logic that returns ISOSCELES regardless of inequality
# --------------------------------------------
def test_isosceles_but_invalid():
    # trian == 1, but a + b <= c
    result1 = Triangle.classify(1, 1, 2)
    assert result1 == Triangle.Type.INVALID

    # trian == 2, but a + c <= b
    result2 = Triangle.classify(1, 3, 1)
    assert result2 == Triangle.Type.INVALID

    # trian == 3, but b + c <= a
    result3 = Triangle.classify(4, 2, 2)
    assert result3 == Triangle.Type.INVALID

# --------------------------------------------
# Test: Floating-point inputs and precision edge cases
# Covers: types and inequality using non-integer inputs
# Kills: arithmetic or comparison mutations involving floats
# --------------------------------------------
def test_floating_point_precision():
    result1 = Triangle.classify(3.5, 3.5, 3.5)
    assert result1 == Triangle.Type.EQUILATERAL

    result2 = Triangle.classify(2.0, 2.0, 3.9)
    assert result2 == Triangle.Type.ISOSCELES

    result3 = Triangle.classify(2.1, 3.2, 4.5)
    assert result3 == Triangle.Type.SCALENE

# --------------------------------------------
# Test: Large valid triangles
# Covers: extreme values that may reveal overflow or logic shortcuts
# --------------------------------------------
def test_large_numbers():
    result1 = Triangle.classify(10000, 10000, 10000)
    assert result1 == Triangle.Type.EQUILATERAL

    result2 = Triangle.classify(100000, 100001, 100002)
    assert result2 == Triangle.Type.SCALENE

if __name__ == "__main__":
    pytest.main()
