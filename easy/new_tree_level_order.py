from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    
    def get_tree_level_traversal(self, root:TreeNode) -> List[int]:

        travel = []

        if root is None:
            return travel
        
        q = deque()

        q.append(root)

        while len(q) > 0:

            current_element = q.popleft()

            travel.append(current_element.val)

            if current_element.left is not None:
                q.append(current_element.left)

            if current_element.right is not None:
                q.append(current_element.right)

        return travel
    
# Create some binary trees for testing

# Tree 1
tree_1 = TreeNode(val=1)
tree_1.left = TreeNode(val=2, left=TreeNode(val=5))
tree_1.left.left.left = TreeNode(val=3, left=TreeNode(val=4))
tree_1.left.left.right = TreeNode(val=6)

s = Solution()
print(s.get_tree_level_traversal(tree_1)) # [1, 2, 5, 3, 6, 4]