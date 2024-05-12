# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteNode(self, node: ListNode):
        
        pointer = node
        
        while pointer != None:
            
            if pointer.next is not None:
        
                pointer.val = pointer.next.val
            
                if pointer.next.next is None:
                    pointer.next = None
            
            pointer = pointer.next