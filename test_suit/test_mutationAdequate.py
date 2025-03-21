import pytest
from isTriangle import Triangle

def test_valid_triangles():
    """Valid triangles (covering all possible paths)"""
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE  # Right triangle
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL  # Equilateral
    assert Triangle.classify(2, 3, 3) == Triangle.Type.ISOSCELES  # Isosceles

def test_invalid_triangles():
    """Test cases where the sides do NOT form a valid triangle."""
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID  # Triangle inequality fails
    assert Triangle.classify(0, 1, 2) == Triangle.Type.INVALID  # Zero length
    assert Triangle.classify(-1, 2, 3) == Triangle.Type.INVALID  # Negative length
    assert Triangle.classify(10, 1, 1) == Triangle.Type.INVALID  # Impossible triangle

def test_edge_cases():
    """Edge conditions that may be affected by mutations."""
    assert Triangle.classify(1, 1, 1) == Triangle.Type.EQUILATERAL  # Smallest valid triangle
    assert Triangle.classify(999, 999, 999) == Triangle.Type.EQUILATERAL  # Large numbers
    assert Triangle.classify(1.5, 2.5, 3.0) == Triangle.Type.SCALENE  # Floating-point triangle

def test_triangle_inequality_failures():
    """Cases that break the triangle inequality rule."""
    assert Triangle.classify(2, 2, 4) == Triangle.Type.INVALID
    assert Triangle.classify(4, 4, 8) == Triangle.Type.INVALID
    assert Triangle.classify(10, 10, 20) == Triangle.Type.INVALID

def test_isosceles_mutation_killers():
    """Specific test cases to detect faulty mutations in isosceles logic."""
    assert Triangle.classify(5, 7, 5) == Triangle.Type.ISOSCELES  # a == c, a + c > b
    assert Triangle.classify(6, 6, 10) == Triangle.Type.INVALID  # Edge case failure
    assert Triangle.classify(5, 10, 5) == Triangle.Type.INVALID  # Edge failure

def test_floating_point_and_large_valid():
    """Floating-point and large values to detect arithmetic-related mutations."""
    assert Triangle.classify(3.5, 3.5, 3.5) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(1.1, 1.1, 1.5) == Triangle.Type.ISOSCELES
    assert Triangle.classify(1000, 1001, 1002) == Triangle.Type.SCALENE

if __name__ == "__main__":
    pytest.main()
