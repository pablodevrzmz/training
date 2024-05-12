
class Solution:

    def firstUniqChar(self, s: str) -> int:

        visited = {}
        
        for i in range(len(s)):

            if i not in visited:

                found = False

                for j in range(i+1,len(s)):
                    
                    if s[i] == s[j]:
                        found = True
                        visited[j] = True

                if not found:
                    return i
            
        return -1
    

s = Solution()

print(s.firstUniqChar("aadadaad"))


'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]] ==1:
                return i
        return -1
'''

