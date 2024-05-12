from typing import List, Dict

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_as_dict: Dict[int,int] = dict()

        for element in nums:

            if element not in nums_as_dict:
                nums_as_dict[element] = element
            else:
                return True

        return False



nums = [1,2,3,4]

s = Solution()

print(s.containsDuplicate(nums))