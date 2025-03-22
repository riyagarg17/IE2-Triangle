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

    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE  # Right triangle
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL  # Equilateral triangle
    assert Triangle.classify(2, 3, 3) == Triangle.Type.ISOSCELES  # Isosceles triangle (b == c)

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
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID  # Triangle inequality fail
    assert Triangle.classify(0, 5, 5) == Triangle.Type.INVALID  # Zero side
    assert Triangle.classify(-1, 2, 3) == Triangle.Type.INVALID  # Negative length
    assert Triangle.classify(10, 1, 1) == Triangle.Type.INVALID  # Impossible triangle, a too large

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
    assert Triangle.classify(1, 1, 1) == Triangle.Type.EQUILATERAL  # Smallest valid triangle
    assert Triangle.classify(999, 999, 999) == Triangle.Type.EQUILATERAL  # Large triangle
    assert Triangle.classify(1.5, 2.5, 3.0) == Triangle.Type.SCALENE  # Floating-point triangle

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
    assert Triangle.classify(2, 2, 4) == Triangle.Type.INVALID  # a + b == c with equal sides
    assert Triangle.classify(4, 4, 8) == Triangle.Type.INVALID  # Edge case for invalid isosceles
    assert Triangle.classify(10, 10, 20) == Triangle.Type.INVALID  # Another edge case of invalid isosceles
    assert Triangle.classify(3, 3, 3.0001) == Triangle.Type.ISOSCELES  # Near-equilateral (float)
    assert Triangle.classify(5, 5, 6) == Triangle.Type.ISOSCELES  # Valid isosceles (a == b)

def test_missing_statement_coverage():
    """
    Specifically targets trian == 2 (a == c) with triangle inequality passed.
    This line was previously uncovered in statement coverage.
    """
    assert Triangle.classify(5, 7, 5) == Triangle.Type.ISOSCELES  # a == c, a + c > b   

if __name__ == "__main__":
    pytest.main()
