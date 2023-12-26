# '''
# Write a Python unit test program to check if a given number is prime or not.
# '''


# Define a function 'is_prime' to check if a number is prime.
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True


'''
Write a Python unit test program to check if a list is sorted in ascending order.
'''

def is_sorted_ascending(lst):
    # Check if all elements at index i are less than or equal to elements at index i+1.
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

