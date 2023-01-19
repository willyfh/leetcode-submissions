# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            ans = ListNode()
            head = ans
            rem = 0
            while l1 != None and l2 != None:
                newNode = ListNode()
                add = l1.val + l2.val + rem
                addVal = add % 10
                rem = add // 10
                newNode.val = addVal
                
                ans.next = newNode
                ans = ans.next
                l1 = l1.next
                l2  = l2.next
                
            while l1 != None:
                newNode = ListNode()
                add  = l1.val + rem
                addVal = add % 10
                rem = add // 10
                newNode.val = addVal
                
                ans.next = newNode
                ans = ans.next
                l1 = l1.next
                
            while l2 != None:
                newNode = ListNode()
                add  = l2.val + rem
                addVal = add % 10
                rem = add // 10
                newNode.val = addVal
                
                ans.next = newNode
                ans = ans.next
                l2 = l2.next
                
            if rem!=0:
                newNode = ListNode(rem)
                ans.next = newNode
                
            return head.next