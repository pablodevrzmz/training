from typing import List

bad_version = 2

def isBadVersion(n: int) -> bool:
    return n >= bad_version

class Solution:

    def firstBadVersion(self, n: int) -> int:

        if n == 1:
            return 1
        
        left , right = 0, n

        while left < right:
            
            mid = (left + right) // 2
            
            if isBadVersion(mid):

                if mid - 1 <= 0 or not isBadVersion(mid - 1):
                    return mid
                
                if mid + 1 <= n and isBadVersion(mid + 1):
                    right = mid - 1

            else:

                if mid + 1 <= n and isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1
                

# Time complexity: O(log n)
# Space complexity: O(1)

# Do some test cases

s = Solution()

n = 2

print(s.firstBadVersion(n))