import pytest
from isTriangle import Triangle

# --------------------------------------------
# NEGATIVE & ZERO LENGTH INPUTS
# --------------------------------------------
def test_negative_or_zero_inputs():
    """
    Covers all paths where any side is zero or negative.
    These immediately return INVALID.
    """
    result1 = Triangle.classify(0, 1, 2)
    assert result1 == Triangle.Type.INVALID    # a = 0

    result2 = Triangle.classify(1, 0, 2)
    assert result2 == Triangle.Type.INVALID    # b = 0

    result3 = Triangle.classify(1, 2, 0)
    assert result3 == Triangle.Type.INVALID    # c = 0

    result4 = Triangle.classify(-1, 2, 3)
    assert result4 == Triangle.Type.INVALID    # a < 0

# --------------------------------------------
# PATHS BASED ON 'trian' VARIABLE VALUE
# --------------------------------------------
def test_trian_variable_paths():
    """
    Covers all decision paths based on 'trian':
    - trian == 0 (no sides equal)
    - trian == 1 (a == b)
    - trian == 2 (a == c)
    - trian == 3 (b == c)
    - trian > 3 (equilateral)
    """
    result1 = Triangle.classify(3, 4, 5)
    assert result1 == Triangle.Type.SCALENE      # trian = 0

    result2 = Triangle.classify(3, 3, 5)
    assert result2 == Triangle.Type.ISOSCELES    # trian = 1

    result3 = Triangle.classify(3, 5, 3)
    assert result3 == Triangle.Type.ISOSCELES    # trian = 2

    result4 = Triangle.classify(5, 3, 3)
    assert result4 == Triangle.Type.ISOSCELES    # trian = 3

    result5 = Triangle.classify(5, 5, 5)
    assert result5 == Triangle.Type.EQUILATERAL  # trian > 3

# --------------------------------------------
# TRIANGLE INEQUALITY FAILURES
# --------------------------------------------
def test_triangle_inequality_failures():
    """
    Tests when the sum of any two sides is not greater than the third.
    These should all return INVALID after trian == 0 check.
    """
    result1 = Triangle.classify(1, 2, 3)
    assert result1 == Triangle.Type.INVALID    # a + b = c

    result2 = Triangle.classify(2, 3, 5)
    assert result2 == Triangle.Type.INVALID    # a + b = c, a bit redundant

    result3 = Triangle.classify(5, 1, 1)
    assert result3 == Triangle.Type.INVALID    # a > b + c

# --------------------------------------------
# ISOSCELES BUT INVALID
# --------------------------------------------
def test_isosceles_but_invalid():
    # Test ISOSCELES conditions with invalid triangle inequality
    result1 = Triangle.classify(5, 5, 10)
    assert result1 == Triangle.Type.INVALID

    result2 = Triangle.classify(10, 5, 5)
    assert result2 == Triangle.Type.INVALID

    result3 = Triangle.classify(5, 10, 5)
    assert result3 == Triangle.Type.INVALID

# --------------------------------------------
# FLOATING POINT & LARGE INPUTS
# --------------------------------------------
def test_floating_point_and_large_valid():
    """
    Covers edge cases for number type and size:
    - Floating-point triangle
    - Large integers
    """
    result1 = Triangle.classify(3.5, 3.5, 3.5)
    assert result1 == Triangle.Type.EQUILATERAL

    result2 = Triangle.classify(1.1, 1.1, 1.5)
    assert result2 == Triangle.Type.ISOSCELES

    result3 = Triangle.classify(1000, 1001, 1002)
    assert result3 == Triangle.Type.SCALENE

if __name__ == "__main__":
    pytest.main()
