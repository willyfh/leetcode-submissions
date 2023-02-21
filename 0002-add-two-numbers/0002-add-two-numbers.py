# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = head = ListNode()
        s = 0
        c = 0
        while l1!=None or l2!=None:
            if l1!=None:
                s += l1.val
                l1 = l1.next
                
            if l2!=None:
                s += l2.val
                l2 = l2.next
            s += c
    
            if s > 9 :
                c = 1
                s -= 10    
            else:
                c =0
            
            ans.next = ListNode(s)
            ans = ans.next
            s = 0
            
            
        if c==1:
            ans.next = ListNode(1)
            
        return head.next