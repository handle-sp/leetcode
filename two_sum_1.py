'''
1. Two Sum

Difficulty: Easy

Description: 

    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add
    up to target.

    You may assume that each input would have exaclty one
    solution, and you may not use the same element twice.

    You can return the answer in any order.
 

   
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_table = {nums[0]: 0}
        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in sum_table:
                return [sum_table[complement], i]
            else:
                sum_table[nums[i]] = i

    def execute(self, nums: List[int], target: int) -> None:
        print(f"nums: {nums}")
        print(f"target: {target}")
        k = self.twoSum(nums, target)
        print(f"k: {k}")
        print(f"output: {k}")
        print("=" * 20)