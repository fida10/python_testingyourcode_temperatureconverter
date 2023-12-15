import pytest
from src.ans import is_prime


def test_is_prime():
    assert is_prime(2)
    assert not is_prime(4)
    assert not is_prime(6)

def test_handle_exception_for_invalid_number():
    with pytest.raises(ValueError):
        is_prime(-1)
        is_prime(-12)
        is_prime(-123)

def test_handle_exception_for_invalid_type():
    with pytest.raises(ValueError):
        is_prime("hello")
        is_prime("world")
        is_prime("123")
        is_prime(False)

if __name__ == '__main__':
    pytest.main()
