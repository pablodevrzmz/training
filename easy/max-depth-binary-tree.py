from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __max_depth_recursive(self,max_depth: int, root: Optional[TreeNode]):

        if root is not None:
            
            max_depth += 1
            
            max_depth_left = self.__max_depth_recursive(max_depth,root.left)
            
            max_depth_right = self.__max_depth_recursive(max_depth,root.right)
            
            if max_depth_left > max_depth:
                max_depth = max_depth_left

            if max_depth_right > max_depth:
                max_depth = max_depth_right

        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return max_depth
        else:
            return self.__max_depth_recursive(max_depth,root)
        

s = Solution()

### test cases

## Empty
assert s.maxDepth(None) == 0

## Non Empty
tree = TreeNode(val=3)
tree.left = TreeNode(val=9)
tree.left.left = TreeNode(val=15)
tree.left.left.left = TreeNode(val=16)

print(s.maxDepth(tree))