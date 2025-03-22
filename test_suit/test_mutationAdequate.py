import pytest
from isTriangle import Triangle

# --------------------------------------------
# Test: Equilateral triangle (all sides equal)
# Covers: trian > 3 condition and correct classification
# --------------------------------------------
def test_equilateral():
    # trian > 3
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL

# --------------------------------------------
# Test: Scalene triangle (all sides different)
# Covers: trian == 0 and passes triangle inequality
# --------------------------------------------
def test_scalene():
    # trian == 0; passes triangle inequality
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE

# --------------------------------------------
# Test: Invalid triangles with zero or negative side lengths
# Covers: Early exit on a <= 0 or b <= 0 or c <= 0
# Also detects mutations that skip these checks
# --------------------------------------------
def test_invalid_negative_and_zero_sides():
    assert Triangle.classify(-1, 2, 3) == Triangle.Type.INVALID
    assert Triangle.classify(0, 4, 5) == Triangle.Type.INVALID
    assert Triangle.classify(5, 0, 3) == Triangle.Type.INVALID
    assert Triangle.classify(4, 5, 0) == Triangle.Type.INVALID

# --------------------------------------------
# Test: Triangles that violate the triangle inequality
# Covers: a + b <= c, a + c <= b, b + c <= a
# Kills mutants in inequality logic
# --------------------------------------------
def test_invalid_triangle_inequality():
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID
    assert Triangle.classify(3, 1, 2) == Triangle.Type.INVALID
    assert Triangle.classify(2, 3, 5) == Triangle.Type.INVALID
    assert Triangle.classify(10, 1, 1) == Triangle.Type.INVALID

# --------------------------------------------
# Test: Isosceles triangle via each trian value (1, 2, 3)
# Covers: trian == 1, 2, 3 and corresponding triangle inequalities
# Kills any mutation that misclassifies isosceles or skips its logic
# --------------------------------------------
def test_isosceles_all_paths():
    # trian == 1 and a + b > c
    assert Triangle.classify(3, 3, 4) == Triangle.Type.ISOSCELES
    # trian == 2 and a + c > b
    assert Triangle.classify(4, 5, 4) == Triangle.Type.ISOSCELES
    # trian == 3 and b + c > a
    assert Triangle.classify(5, 4, 4) == Triangle.Type.ISOSCELES

# --------------------------------------------
# Test: Isosceles shape but fails triangle inequality
# Covers: correct fallback to INVALID instead of ISOSCELES
# Kills: incorrect logic that returns ISOSCELES regardless of inequality
# --------------------------------------------
def test_isosceles_but_invalid():
    # trian == 1, but a + b <= c
    assert Triangle.classify(1, 1, 2) == Triangle.Type.INVALID
    # trian == 2, but a + c <= b
    assert Triangle.classify(1, 3, 1) == Triangle.Type.INVALID
    # trian == 3, but b + c <= a
    assert Triangle.classify(4, 2, 2) == Triangle.Type.INVALID

# --------------------------------------------
# Test: Floating-point inputs and precision edge cases
# Covers: types and inequality using non-integer inputs
# Kills: arithmetic or comparison mutations involving floats
# --------------------------------------------
def test_floating_point_precision():
    assert Triangle.classify(3.5, 3.5, 3.5) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(2.0, 2.0, 3.9) == Triangle.Type.ISOSCELES
    assert Triangle.classify(2.1, 3.2, 4.5) == Triangle.Type.SCALENE

# --------------------------------------------
# Test: Large valid triangles
# Covers: extreme values that may reveal overflow or logic shortcuts
# --------------------------------------------
def test_large_numbers():
    assert Triangle.classify(10000, 10000, 10000) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(100000, 100001, 100002) == Triangle.Type.SCALENE

if __name__ == "__main__":
    pytest.main()
