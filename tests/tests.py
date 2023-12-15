import pytest
from src.ans import is_prime


def test_is_prime():
    assert is_prime(2)
    assert not is_prime(4)
    assert not is_prime(6)

def test_handle_exception_for_invalid_number_negative():
    with pytest.raises(ValueError):
        is_prime(-12)

def test_handle_exception_for_invalid_number_decimal():
    with pytest.raises(ValueError):
        is_prime(32.45)
        

def test_handle_exception_for_invalid_type_string():
    with pytest.raises(ValueError):
        is_prime("hello")
        is_prime("world")

def test_handle_exception_for_invalid_type_bool():
    with pytest.raises(ValueError):
        is_prime(False)

        
def test_handle_exception_for_invalid_type_num_as_string():
    with pytest.raises(ValueError):
        is_prime("123")



if __name__ == '__main__':
    pytest.main()
