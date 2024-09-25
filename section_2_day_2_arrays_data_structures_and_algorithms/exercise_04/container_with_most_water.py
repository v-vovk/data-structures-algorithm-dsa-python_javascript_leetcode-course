# Container With Most Water
from typing import List


# Question
# https://leetcode.com/problems/container-with-most-water/description/

# Container with most Water - You are given an integer array height of length n. There are n vertical lines drawn such
# that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis
# form a container, such that the container contains the most water (depth is constant across containers). Return the
# area (that the 2 lines and the X axis make) of container which can store the max amount of water. Notice that you may
# not slant the container.

# Solution 1
# Brute force method - Time = O(n^2) Space = O(1)
def maxArea(self, height: List[int]) -> int:
    area = 0
    for i in range(0, len(height) - 1):
        for j in range(i + 1, len(height)):
            temp = min(height[i], height[j]) * (j - i)
            area = max(temp, area)

    return area


# Solution 2
# Two pointer method - Time = O(n) Space = O(1)
def max_area_optimum(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Best solution from LeetCode
def maxArea(height: List[int]) -> int:
    maxH, maxA, left, right = max(height), 0, 0, len(height) - 1
    while left < right:
        if height[left] < height[right]:
            if height[left] * (right - left) > maxA:
                maxA = height[left] * (right - left)
        else:
            if height[right] * (right - left) > maxA:
                maxA = height[right] * (right - left)

        if maxH * (right - left) <= maxA:
            break

        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1

    return maxA
