from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:

        n = len(nums)
        i = 0

        while i < n:

            if nums[i] == 0:

                for j in range(i+1,n):
                    
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
            i += 1
                        

nums = [1,2,3,4,5,0]
s = Solution()
s.moveZeroes(nums)
print(nums)