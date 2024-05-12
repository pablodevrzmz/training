from typing import List

end = "_end"

class Solution:

    def __make_trie(self, strs: List[str]):
        trie_dict = dict()

        for word in strs:
            current_root = trie_dict
            for letter in word:
                current_root = current_root.setdefault(letter,{})
            current_root[end] = end
        return trie_dict

    def longestCommonPrefix(self, strs: List[str]) -> str:

        list_as_trie = self.__make_trie(strs)

        if end in list_as_trie: # empty string in there
            return ""
        
        prefix = ""

        root = list_as_trie

        while len(root.keys()) == 1:
            key = list(root.keys())[0]
            if key != end:
                prefix += key
                root = root[key]
            else:
                root = {}

        return prefix


s = Solution()

strs = [""]

print(s.longestCommonPrefix(strs))


'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        common = strs[0]
        for i in strs:
            if common == "":
                return ""
            newcommon = ""
            for j in range(len(common)):
                if j < len(i):
                    if i[j] == common[j]:
                        newcommon += i[j]
                    else:
                        common = newcommon
                        break
                else:
                    common = newcommon
                    break
        return common
'''


        