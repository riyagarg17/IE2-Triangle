import pytest
from isTriangle import Triangle

def test_valid_triangles():
    """Test cases where the sides form a valid triangle."""
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE  # Right triangle
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL  # Equilateral
    assert Triangle.classify(2, 3, 3) == Triangle.Type.ISOSCELES  # Isosceles

def test_invalid_triangles():
    """Test cases where the sides do NOT form a valid triangle."""
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID  # Triangle inequality fail
    assert Triangle.classify(0, 5, 5) == Triangle.Type.INVALID  # Zero length
    assert Triangle.classify(-1, 2, 3) == Triangle.Type.INVALID  # Negative length
    assert Triangle.classify(10, 1, 1) == Triangle.Type.INVALID  # Impossible triangle

def test_edge_cases():
    """Test cases for edge conditions."""
    assert Triangle.classify(1, 1, 1) == Triangle.Type.EQUILATERAL  # Smallest valid triangle
    assert Triangle.classify(999, 999, 999) == Triangle.Type.EQUILATERAL  # Large triangle
    assert Triangle.classify(1.5, 2.5, 3.0) == Triangle.Type.SCALENE  # Floating-point triangle

def test_extra_cases_for_full_coverage():
    """Additional test cases to reach 95%+ coverage."""
    assert Triangle.classify(2, 2, 4) == Triangle.Type.INVALID  # Triangle inequality fail with Isosceles-like input
    assert Triangle.classify(4, 4, 8) == Triangle.Type.INVALID  # Edge case for invalid isosceles
    assert Triangle.classify(10, 10, 20) == Triangle.Type.INVALID  # Another edge case of invalid isosceles
    assert Triangle.classify(3, 3, 3.0001) == Triangle.Type.ISOSCELES  # Floating point close to Equilateral
    assert Triangle.classify(5, 5, 6) == Triangle.Type.ISOSCELES  # Standard Isosceles
    

if __name__ == "__main__":
    pytest.main()
