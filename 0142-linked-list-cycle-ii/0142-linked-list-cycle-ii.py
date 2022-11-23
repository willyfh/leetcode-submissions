# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow = head
        fast = head
        
        cycle=False
        while fast!=None and fast.next != None:
            
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
                
        if cycle:
            slow = head
            
            while slow!=fast:
                slow = slow.next
                fast = fast.next
                
            return slow
        else:
            return None