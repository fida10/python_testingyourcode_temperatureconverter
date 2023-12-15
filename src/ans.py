""" 
Practice Question 3: Prime Number Checker

Task:
Write a function is_prime that takes an integer and returns True 
if the number is prime, and False otherwise. Store the function in a module called prime_checker.py.

Unit Test for Prime Number Checker:

Create a file test_prime_checker.py for testing.
"""


def is_prime(candidate):
    if not type(candidate) is int: # necessary since bool is a subclass of int, so checking explicitly for int
        raise ValueError(f"{candidate} - this is not a number!")
    elif candidate < 0:
        raise ValueError(f"{candidate} - this is a negative number!")
    
    for i in range(2, (candidate // 2) + 1):
        if candidate % i == 0:
            return False
    return True
