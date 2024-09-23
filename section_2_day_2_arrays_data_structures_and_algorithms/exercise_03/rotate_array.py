# Coding Exercise - Python: Rotate Array
from typing import List


# Question
# https://leetcode.com/problems/rotate-array/description/

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Solution

# Bruteforce
def rotate_array(array, k):
    if len(array) == 0: return []

    k = k % len(array)
    temp = array[-k:]
    for i in reversed(range(0, len(array) - k)):
        array[i + k] = array[i]
    for i in range(len(temp)):
        array[i] = temp[i]
    return array


print(rotate_array([1, 2, 3, 4, 5], 3))


# Optimised
def reverse(array, start, end):
    while (start < end):
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


def rotate_array(array, k):
    if len(array) == 0: return []

    k = k % len(array)
    reverse(array, 0, len(array) - 1)
    reverse(array, 0, k - 1)
    reverse(array, k, len(array) - 1)
    return array


print(rotate_array([1, 2, 3, 4, 5], 3))


# best from leetcode
def rotate(nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
