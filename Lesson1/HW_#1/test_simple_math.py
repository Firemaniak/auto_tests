import pytest
from simple_math import SimpleMath

# Sim_math = SimpleMath()

@pytest.fixture
def fixture():
    return SimpleMath()

def test_scuare(fixture):
    res = fixture.square(2)
    assert res == 4

def test_cube(fixture):
    res = fixture.cube(-3)
    assert res == -27