# Coding Exercise - Python: Monotonic Array
from typing import List


# Question
# https://leetcode.com/problems/monotonic-array

# An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if
# all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left
# to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise.

# Solution

def monotonic_array(array):
    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasing = False
        if array[i] > array[i - 1]:
            decreasing = False

    return increasing or decreasing

# from LeetCode best solution:
def is_monotonic(self, nums: List[int]) -> bool:
    inc = True
    dec = True
    prev = nums[0]

    # check inc
    for num in nums[1:]:
        if prev < num:
            inc = False
            break
        prev = num

    # check dec
    prev = nums[0]
    for num in nums[1:]:
        if prev > num:
            dec = False
            break
        prev = num
    return inc or dec