# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next !=None:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        
        slow = head
        prev = None
        
        while slow!=second:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        first = prev
        
        ans = 0
        while second!=None:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next
            
        return ans