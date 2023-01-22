# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        slow = head
        fast = head
        
        i=0
        while i <n:
            fast = fast.next
            i+=1
            continue
        if fast == None: # the head is removed
                return slow.next
        while fast.next != None:

            slow = slow.next
            fast = fast.next
        
                
        slow.next = slow.next.next
        
        return head
        