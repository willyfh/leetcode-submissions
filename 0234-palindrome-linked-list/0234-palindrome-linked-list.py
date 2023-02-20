# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        slow = head
        fast = head
        
        while fast != None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow !=None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
            
        while prev!=None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
        
        