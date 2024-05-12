from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

class Solution:

    def __is_valid_bts(self, root: Optional[TreeNode], arr: List[int] = []):
        
        if root is not None:

            self.__is_valid_bts(root.left,arr)

            if len(arr) > 0 and root.val <= arr[len(arr)-1]:
                raise Exception( f"Invalid binary search tree. Root {root.val}, arr = {arr}")
                
            arr.append(root.val)

            self.__is_valid_bts(root.right,arr)

        return arr


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        try:
            self.__is_valid_bts(root,[])
            return True
        except Exception as e:
            print(e)
            return False
    
    

## Test cases
    
s = Solution()

# assert s.isValidBST(None) == True

tree = TreeNode(left=TreeNode(val=1),val=2,right=TreeNode(val=3))

# assert s.isValidBST(tree) == True

tree_2 = TreeNode(left=TreeNode(val=4),val=5,right=TreeNode(val=4))
tree_2.right.left = TreeNode(val=3)
tree_2.right.right = TreeNode(val=6)

# assert s.isValidBST(tree_2) == False

tree_3 = TreeNode(val=0)

assert s.isValidBST(tree_3) == True