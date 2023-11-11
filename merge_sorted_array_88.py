'''
88. Merge Sorted Array

Difficulty: 88

Description: 

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing
    order, and two integers m and n, representing the number of elements
    in nums1 and nums2 respectively. 

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but 
    instead be stored inside the array nums1. To accomodate this, nums1 has
    a length of m + n, where the first m elements denote the elements 
    that should be merged, and the last n elements are set to 0 and should be
    ignored. nums2 has a length of n.
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """           
        # 1. Handle for the case when nums2 has no values or n equals 0.
        #    This means there is no second list to merge with our first.
        if len(nums2) == 0 or n == 0:
            return
        
        # initialize index_of_m to track the current index in nums1
        index_of_m = len(nums1) - n - 1

        # initialize index_of_n to track the current index in nums2
        index_of_n = n - 1

        # iterate over our nums1 list in reverse order
        for sort_index in range(len(nums1) - 1, -1, -1):
            if index_of_m >= 0 and index_of_n >= 0:
                if nums2[index_of_n] >= nums1[index_of_m]:
                    nums1[sort_index] = nums2[index_of_n]
                    index_of_n -= 1
                else:
                    nums1[sort_index] = nums1[index_of_m]
                    index_of_m -= 1
            elif index_of_m < 0:
                nums1[sort_index] = nums2[index_of_n]
                index_of_n -= 1
            else:
                break
