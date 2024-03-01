# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        reverse = copy.deepcopy(head)
        prev = None
        while reverse!=None:
            next = reverse.next
            reverse.next = prev
            prev = reverse
            reverse =next
        ans = 0
        reverse = prev
        while head != None:
            ans = max(ans, head.val+reverse.val) 
            head = head.next
            reverse = reverse.next
        return ans