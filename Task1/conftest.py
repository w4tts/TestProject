import pytest
import random


@pytest.fixture(scope="function")
def random_number():
    number = random.randint(1, 5)
    return number


@pytest.fixture(scope="session")
def random_number_2():
    number_s = random.randint(1, 500)
    return number_s
