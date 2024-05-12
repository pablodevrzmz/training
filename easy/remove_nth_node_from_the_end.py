from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return self.val
        
        
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        for i in range(n):
            
            print(second.val,i)
             
            # If count of nodes in the 
            # given list is less than 'n'
            if(second.next == None):
                 
                # If index = n then 
                # delete the head node
                if(i == n - 1):
                    head = head.next
                return head
            second = second.next
            
         
        while(second.next != None):
            second = second.next
            first = first.next
         
        first.next = first.next.next
        
        return head