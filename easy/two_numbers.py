from typing import List, Dict

class Solution:

    # 2 O(n) ~ O(2n) ~ O(n)

    def __map_to_dict(self, nums: List[int], target: int)-> Dict[int,List[int]]:

        # O(n) time and space
        sol_dict: Dict[int,List[int]] = dict()

        for index in range(len(nums)):
            current_num = nums[index]
            if current_num not in sol_dict:
                sol_dict[current_num] = [index]
            else:
                sol_dict[current_num].append(index)
        return sol_dict

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_as_map = self.__map_to_dict(nums,target)

        # O(n) time and space
        for num in nums:

            operand_to_find = target - num

            if operand_to_find == num and len(nums_as_map[num]) > 1:
                return [nums_as_map[num][0],nums_as_map[num][1]]
            elif operand_to_find != num and operand_to_find in nums_as_map:
                return [nums_as_map[num][0],nums_as_map[operand_to_find][0]]
            
        raise Exception(f"Nums array has not a valid solution: {nums}")
    
s = Solution()

nums = [-3,4,3,90]

target = 0

print(s.twoSum(nums,target))