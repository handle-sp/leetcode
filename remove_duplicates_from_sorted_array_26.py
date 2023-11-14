'''
26. Remove Duplicates from Sorted Array

Difficulty: Easy

Description: 

    Given an integer array nums sorted in non-descending order, remove the duplicates
    in-place such that each unique element appears only once. The relative order
    of elements should be kept the same. Then return the number of unique elements
    in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you
    need to do the following things:

     - Change the array nums such that the first k elements of nums contain the 
     unique elements in the order they were present in nums initially. The 
     remaining elements of nums are not important as well as the size of nums.

     - Return k.
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_index = 0
        last_unique_number = None
        for i in range(len(nums)):            
            if nums[i] != last_unique_number:
                last_unique_number = nums[i]
                nums[next_index], nums[i] = nums[i], nums[next_index]
                next_index += 1
        return next_index


    def execute(self, nums: List[int]) -> None:
        print(f"before remove duplicates: {nums}")
        k = self.removeDuplicates(nums)
        print(f"k: {k}")
        print(f"after remove duplicates: {nums}")
        print("=" * 20)