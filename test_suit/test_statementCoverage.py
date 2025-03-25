import pytest
from isTriangle import Triangle

# --------------------------------------------
# VALID TRIANGLE TESTS
# --------------------------------------------
def test_valid_triangles():
    """
    Covers valid triangle classifications:
    - SCALENE: all sides different
    - EQUILATERAL: all sides equal
    - ISOSCELES: two sides equal
    """
    result1 = Triangle.classify(3, 4, 5)
    assert result1 == Triangle.Type.SCALENE  # Right triangle

    result2 = Triangle.classify(5, 5, 5)
    assert result2 == Triangle.Type.EQUILATERAL  # Equilateral triangle

    result3 = Triangle.classify(2, 3, 3)
    assert result3 == Triangle.Type.ISOSCELES  # Isosceles triangle (b == c)

# --------------------------------------------
# INVALID TRIANGLE TESTS
# --------------------------------------------
def test_invalid_triangles():
    """
    Covers inputs that should return INVALID due to:
    - triangle inequality violation
    - zero or negative side lengths
    - long side vs short sides
    """
    result1 = Triangle.classify(1, 2, 3)
    assert result1 == Triangle.Type.INVALID  # Triangle inequality fail

    result2 = Triangle.classify(0, 5, 5)
    assert result2 == Triangle.Type.INVALID  # Zero side

    result3 = Triangle.classify(-1, 2, 3)
    assert result3 == Triangle.Type.INVALID  # Negative length

    result4 = Triangle.classify(10, 1, 1)
    assert result4 == Triangle.Type.INVALID  # Impossible triangle, a too large

# --------------------------------------------
# EDGE CASES: extremes & floating points
# --------------------------------------------
def test_edge_cases():
    """
    Covers:
    - smallest possible valid triangle
    - very large values
    - floating-point input handling
    """
    result1 = Triangle.classify(1, 1, 1)
    assert result1 == Triangle.Type.EQUILATERAL  # Smallest valid triangle

    result2 = Triangle.classify(999, 999, 999)
    assert result2 == Triangle.Type.EQUILATERAL  # Large triangle

    result3 = Triangle.classify(1.5, 2.5, 3.0)
    assert result3 == Triangle.Type.SCALENE  # Floating-point triangle

# --------------------------------------------
# ADDITIONAL INVALID CASES & EDGE CONDITIONS
# --------------------------------------------
def test_extra_cases_for_full_coverage():
    """
    Adds missing statement/edge coverage:
    - isosceles shape that fails triangle inequality
    - nearly equilateral but floating point
    - validates trian paths
    """
    result1 = Triangle.classify(2, 2, 4)
    assert result1 == Triangle.Type.INVALID  # a + b == c with equal sides

    result2 = Triangle.classify(4, 4, 8)
    assert result2 == Triangle.Type.INVALID  # Edge case for invalid isosceles

    result3 = Triangle.classify(10, 10, 20)
    assert result3 == Triangle.Type.INVALID  # Another edge case of invalid isosceles

    result4 = Triangle.classify(3, 3, 3.0001)
    assert result4 == Triangle.Type.ISOSCELES  # Near-equilateral (float)

    result5 = Triangle.classify(5, 5, 6)
    assert result5 == Triangle.Type.ISOSCELES  # Valid isosceles (a == b)

# --------------------------------------------
# TARGETING PREVIOUSLY UNCOVERED STATEMENT
# --------------------------------------------
def test_missing_statement_coverage():
    """
    Specifically targets trian == 2 (a == c) with triangle inequality passed.
    This line was previously uncovered in statement coverage.
    """
    result = Triangle.classify(5, 7, 5)
    assert result == Triangle.Type.ISOSCELES  # a == c, a + c > b   

if __name__ == "__main__":
    pytest.main()
