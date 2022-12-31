"""https://leetcode.com/problems/two-sum/

"""
from typing import List

"""Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force O(N2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # O(N) ST complexity , better approach
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target-nums[i]]]
            hashmap[nums[i]] = i

        # Nothing is mentioned about array, we can sort it and use two pointers technique to find the solution , however
        # keep in mind that after sorting the array indexes will change
        # nums.sort()
        # start = 0
        # end = len(nums) - 1
        # while start < end:
        #     if nums[start] + nums[end] == target:
        #         return [start, end]
        #     elif nums[start] + nums[end] < target:
        #         start += 1
        #     elif nums[start] + nums[end] > target:
        #         end -= 1


slc_leet_code_1 = Solution()
print(slc_leet_code_1.twoSum(nums=[3,2,4], target=6))
