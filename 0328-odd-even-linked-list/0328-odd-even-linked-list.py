# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        odd = head
        even = head.next
        curr = odd
        curr2 = even
        while curr.next!=None and curr2.next!=None:
            curr.next = curr.next.next
            curr2.next = curr2.next.next
            
            curr2 = curr2.next
            if curr.next == None:
                break
            curr = curr.next
                        
        curr.next = even

        return odd