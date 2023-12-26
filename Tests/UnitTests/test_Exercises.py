import pytest

# from Tests.Exercises import is_prime, is_sorted_ascending

# nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# nums = [4, 6, 8, 10, 12, 14, 16, 18, 20]
# @pytest.mark.is_prime
# def test_is_prime(subtests):
#     for i in nums:
#         with subtests.test(f"testing if {i} is a prime number"):
#             assert is_prime(i)

# @pytest.mark.is_prime
# @pytest.mark.parametrize("i",nums,ids=lambda i: f"testing if {i} is a prime number")
# def test_is_prime(i):
#     assert is_prime(i)


from Tests.Exercises import is_sorted_ascending

# @pytest.mark.is_sorted_ascending
# def test_is_sorted_ascending(subtests):
#     assert is_sorted_ascending(lss)

@pytest.mark.is_sorted_ascending
@pytest.mark.parametrize("lss",([1,12,9,15],))
def test_is_sorted_ascending(lss):
    assert is_sorted_ascending(lss)
