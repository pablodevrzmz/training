from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1

        digits[i] += 1
        
        while i >= 0 and digits[i] == 10:
                
            digits[i] = 0

            if i == 0:
                digits.insert(0,1)
            else:
                digits[i-1] = digits[i-1] + 1

            i -= 1

        return digits
        



s = Solution()

print(s.plusOne([-1]))