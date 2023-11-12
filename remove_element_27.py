'''
27. Remove Element

Difficulty: Easy

Description: 

    Given an integer array nums and an integer val, remove
    all occurrences of val in nums in-place. The order of the 
    elements may be changed. Then return the number of elements 
    in nums which are not equal to val.

    Consider the number of elements in nums which are not equal
    to val to be k, to get accepted, you need to do the following
    things:

    - Change the array nums such that the first k elements of nums
    contain the elements which are not equal to val. The remaining
    elements of nums are not important as well as the size of nums.

    - Return k.
'''

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Step backwards through nums list
        # Store the index of the last item not equal to val to remove, initialize to None.
        non_val = len(nums) - 1
        for i in range(len(nums) - 1, -1 , -1):
            # Check if item at current index is equal to val to remove
            if nums[i] == val:
                # Remove val and check if we can swap with index of last non-val
                nums[i] = None
                if i != non_val:
                    nums[i], nums[non_val] = nums[non_val], nums[i]
                non_val -= 1

        # 4. Return the count of all elements not equal to val.
        return (non_val + 1)

    def execute(self, nums: List[int], val: int) -> None:
        print(f"nums: {nums}")
        print(f"element to remove: {val}")
        k = self.removeElement(nums, val)
        print(f"k: {k}")
        print(f"nums: {nums}")
        print("=" * 20)