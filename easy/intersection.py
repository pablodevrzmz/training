from typing import List

class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = []

        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]: i += 1
            elif nums1[i] > nums2[j]: j += 1
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1

        return intersection         
                

s = Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(s.intersect(nums1, nums2))