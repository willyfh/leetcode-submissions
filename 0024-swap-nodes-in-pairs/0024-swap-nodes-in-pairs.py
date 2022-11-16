# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        curr = head
        prevprev = None
        prev = curr
        curr = curr.next
        head = curr
        
        while prev!=None and prev.next != None:
            temp = curr.next
            curr.next = prev
            prev.next = temp
            
            if prevprev != None:
                prevprev.next = curr
            prevprev = prev
            prev = prev.next
            if prev!=None:
                curr = prev.next
        return head
        