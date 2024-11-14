import pytest
from my_arithmetic_svalerio import pgcd

def test_pgcd():
    assert pgcd(56, 98) == 14
    assert pgcd(101, 10) == 1
    assert pgcd(30, 45) == 15
    assert pgcd(13, 13) == 13
    assert pgcd(0, 5) == 5
