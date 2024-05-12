from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:

    def __run_recursive_swap(self, root: TreeNode):

        if root is None:
            return
        
        root.left, root.right = root.right, root.left

        self.__run_recursive_swap(root.left)
        self.__run_recursive_swap(root.right)

    def __run_in_order_traversal(self, root: TreeNode, traversal: List[int]) -> None:

        if root is None:
            return

        self.__run_in_order_traversal(root.left, traversal)
        
        traversal.append(root.val)
        
        self.__run_in_order_traversal(root.right, traversal)

    def __get_tree_from_input(self, indexes: List[List[int]]) -> TreeNode:

        if len(indexes) == 0:
            return None
        
        root = TreeNode(val=1)

        nodes = deque()

        pointer = 0

        nodes.append(root)

        while pointer < len(indexes):

            current = nodes.popleft()

            left = indexes[pointer][0]
            right = indexes[pointer][1]

            if left != -1:
                current.left = TreeNode(val=left)
                nodes.append(current.left)

            if right != -1:
                current.right = TreeNode(val=right)
                nodes.append(current.right)

            pointer += 1

    def swap_nodes(self, indexes, queries):

        root = self.__get_tree_from_input(indexes)

        initial_depth = 1 # root is at depth 1

        queue = deque()

        queue.append((root, initial_depth))

        traversal = []

        while len(queue) > 0:

            current, depth = queue.popleft()

            if depth in queries:
                self.__run_recursive_swap(current)
                traversal.append(self.__run_in_order_traversal(current, []))

            if current.left is not None:
                queue.append((current.left, depth + 1))

            if current.right is not None:
                queue.append((current.right, depth + 1))
        