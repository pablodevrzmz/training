from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        level_order_traversal = []

        q = deque()

        if root is not None:
            q.append(root)

        while len(q) > 0:

            local_nodes: List[TreeNode] = []
            local: List[int] = []

            try:
                while True:
                    current: TreeNode = q.popleft()
                    local.append(current.val)
                    local_nodes.append(current)
            except:
                pass

            level_order_traversal.append(local)

            for i in local_nodes:

                if i.left is not None:
                    q.append(i.left)
                if i.right is not None:
                    q.append(i.right)

        return level_order_traversal




        