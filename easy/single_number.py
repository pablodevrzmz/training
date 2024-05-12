from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        
        nums_as_dict = {}
        for value in nums:
            if value not in nums_as_dict:
                nums_as_dict[value] = 1
            else:
                nums_as_dict[value] +=1

        return list([n for n in nums if nums_as_dict[n] == 1])[0]
    


s = Solution()

nums = [4,1,2,1,2]

print(s.singleNumber(nums))
