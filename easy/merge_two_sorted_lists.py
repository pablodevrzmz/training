from typing import Optional

class ListNode:

    def __init__(self, val=None, next=None):
         self.val = val
         self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next if self.next is not None else ''}"
    
class Solution:


    def __add(self, merged_list_head: ListNode,next_node: ListNode,val):
        if merged_list_head is None:
            merged_list_head = ListNode(val=val)
        elif next_node is None:
            merged_list_head.next = ListNode(val=val)
            next_node = merged_list_head.next
        else:
            next_node.next = ListNode(val=val)
            next_node = next_node.next
        return merged_list_head, next_node

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged_list_head: ListNode = None

        next_node: ListNode = None

        current: ListNode = list1

        target: ListNode = list2

        while target is not None and current is not None:
            
            while current.val <= target.val:
  
                merged_list_head,next_node = self.__add(merged_list_head,next_node,current.val)

                current = current.next

                if current is None or target.next is None:
                    break
                    
            current, target = target, current


        while current is not None:
            merged_list_head,next_node = self.__add(merged_list_head,next_node,current.val)
            current = current.next

        while target is not None:
            merged_list_head,next_node = self.__add(merged_list_head,next_node,target.val)
            target = target.next

        return merged_list_head
    
s = Solution()

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(4)

merged_list = s.mergeTwoLists(list1,list1)

print(merged_list)