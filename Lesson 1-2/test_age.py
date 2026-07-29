from age import Age_Validator
import pytest

@pytest.fixture
def fixture():
    return Age_Validator()


def test_is_not_adult(fixture):
    assert fixture.is_adult(17) is False


def test_is_adult(fixture):
    assert fixture.is_adult(18) is True
    assert fixture.is_adult(19) is True

