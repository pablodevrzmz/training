from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:

    def __reverseListRecursive(self, head: Optional[ListNode], newHead: ListNode = ListNode()) -> Optional[ListNode]:

        n: ListNode = None

        # Last node, create a new head node with the last one
        if head.next is None:
            newHead.val = head.val
            return newHead
        else:
            n = self.__reverseListRecursive(head.next, newHead)

        n.next = ListNode(head.val)

        return n.next


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return head
        newHead = ListNode()
        self.__reverseListRecursive(head,newHead)
        return newHead
    
s = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

reversed = s.reverseList(head)

print(reversed)