# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergesort(node):
            if node==None or node.next == None:
                return node
            
            left = node
            right = node
            
            prev = left
            while right!=None and right.next!=None:
                prev = left
                left = left.next
                right = right.next.next
            
            prev.next = None
            right = left
            left = node

            left = mergesort(left)
            right = mergesort(right)
            
            return merge(left, right)
        
        def merge(left, right):
            temp = ListNode()
            ret = temp
            while left!=None and right!=None:
                if left.val < right.val:
                    temp.next = ListNode(left.val)
                    left = left.next
                    temp = temp.next
                else:
                    temp.next = ListNode(right.val)
                    right = right.next
                    temp = temp.next
                    
            while left!=None:
                temp.next = ListNode(left.val)
                left = left.next
                temp = temp.next
            
            while right!=None:
                temp.next = ListNode(right.val)
                right = right.next
                temp = temp.next

            return ret.next
        return mergesort(head)
