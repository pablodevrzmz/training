from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    def __str__(self):
        return f"{self.val}"

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.__is_symmetric(root.right,root.left)

    def __is_symmetric(self,node_1: Optional[TreeNode], node_2: Optional[TreeNode]):
        
        result = True

        if node_1 is None and node_2 is not None or node_2 is None and node_1 is not None:
            print("False scenario 1: (",node_1,",",node_2,")")
            result = False
        elif node_1 is not None and node_2 is not None and node_1.val != node_2.val:
            print("False scenario 2: (",node_1,",",node_2,")")
            result = False

        if node_1 is not None and node_2 is not None:
            return result and self.__is_symmetric(node_1.left,node_2.right) and self.__is_symmetric(node_1.right,node_2.left)
        else:
            return result
    

## Test cases
    
s = Solution()

tree_1 = TreeNode(left=TreeNode(val=2),val=1,right=TreeNode(2))

assert s.isSymmetric(tree_1) == True

tree_2 = TreeNode(left=TreeNode(val=2),val=1,right=TreeNode(2))
tree_2.left.left = TreeNode(val=3)
tree_2.left.right = TreeNode(val=4)
tree_2.right.right = TreeNode(val=3)
tree_2.right.left = TreeNode(val=4)

assert s.isSymmetric(tree_2) == True

tree_3 = TreeNode(left=TreeNode(val=2),val=1,right=TreeNode(2))
tree_3.left.right = TreeNode(val=3)
tree_3.left.right = TreeNode(val=3)

assert s.isSymmetric(tree_3) == False


        
        