import math

import pytest


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    num = 7
    assert 7 * 7 == 40


def test_quality():
    assert 10 == 11


@pytest.mark.greater
def test_greater_than_200(subtests):
    for base in range(1, 11):
        with subtests.test(msg=f"running test {base} in power of 5 is greater then 200"):
            result = math.pow(base, 5)
            assert result > 200

    # with subtests.test("assadas"):
    #     assert math.pow(2, 5) > 200
    # with subtests.test("asdasdasd"):
    #     assert math.pow(3, 5) > 200


@pytest.mark.greater
def test_greater_than_300(subtests, input_value):
    for base in range(1, 11):
        with subtests.test(f"running test {base} in power of 5 is greater then {input_value}"):
            result = math.pow(base, 5)
            assert result > input_value
    #
    # with subtests.test("checking if 2^5 is greater than 300"):
    #     assert math.pow(2, 5) > 300
    # with subtests.test("checking if 2^5 is greater than 300"):
    #     assert math.pow(3, 5) > 300

@pytest.mark.greater
@pytest.mark.parametrize("base",range(1,101),ids=lambda base: f"running test {base} in power of 5 is greater then 300")
def test_greater_than_300(base,input_value):
    result = math.pow(base, 5)
    assert result > input_value


@pytest.mark.test_fixtures
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


@pytest.mark.test_fixtures
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0


if __name__ == '__main__':
    pytest.console_main()
