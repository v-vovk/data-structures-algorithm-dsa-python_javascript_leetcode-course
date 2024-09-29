# Two Sum
from typing import List


# Question
# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution 1 - Brute force method - Time = O(n^2) Space = O(1)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    if len(nums) <= 1:
        return []

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# Solution 2 - Hash table method - Time = O(n) Space = O(n)
def two_sum(self, nums: List[int], target: int) -> List[int]:
    num_available = {}

    for i in range(len(nums)):
        needed_val = target - nums[i]
        if needed_val in num_available:
            return [i, num_available[needed_val]]
        else:
            num_available[nums[i]] = i

    return []

# Best solution from LeetCode
def twoSum(self, nums: List[int], target: int) -> List[int]:
    indexMap = {}

    for i, n in enumerate(nums):
        numReq = target - n
        if numReq in indexMap:
            return [i, indexMap[numReq]]
        indexMap[n] = i
