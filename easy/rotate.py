from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for step in range(k):
            element = nums.pop(len(nums)-1)
            nums.insert(0,element)



s = Solution()

nums = [1,2,3,4,5,6,7,8]
k = 5

s.rotate(nums,k)

print(nums)

