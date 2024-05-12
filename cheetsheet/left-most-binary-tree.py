
from typing import List

# find the index of where the target should be if it doesn't exist. 

def searchRange(self, nums: List[int], target: int) -> List[int]:
    
    def binarySearch(nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while (l < r):
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            else: r = m
        return l
        
    l = binarySearch(nums, target)
    # target does not exist. No need to look for the last position.
    if l == len(nums) or nums[l] != target: 
        return [-1, -1]
    # look for the index of target + 1
    r = binarySearch(nums, target + 1)
    # last position is r - 1. 
    return [l, r - 1]