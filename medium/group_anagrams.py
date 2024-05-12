from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = []

        if len(strs) == 0:
            return grouped
        
        used = [0]*len(strs)

        sorted_strs_cache = {}

        for i in range(len(strs)):
            if used[i] == 0:

                local_group = [strs[i]]

                used[i]=1

                if strs[i] not in sorted_strs_cache:
                    sorted_strs_cache[strs[i]] = sorted(strs[i])

                for j in range(i+1, len(strs)):

                    if strs[j] not in sorted_strs_cache:
                        sorted_strs_cache[strs[j]] = sorted(strs[j])

                    if used[j] == 0 and sorted_strs_cache[strs[i]] == sorted_strs_cache[strs[j]]:
                        local_group.append(strs[j])
                        used[j]=1

                grouped.append(local_group)

        return grouped