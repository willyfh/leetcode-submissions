# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            node = ListNode(0)
            result = node
            while left!=None and right!=None:
                if left.val < right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
                node = node.next
                
            if left !=None:
                node.next = left
            if right !=None:
                node.next = right
                
            return result.next
        
        def mergesort(node):
            if node==None or node.next == None:
                return node
            
            slow = node
            fast = node
            
            while fast != None and fast.next!=None:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            right = slow
            left = node 
            
            left = mergesort(left)
            right = mergesort(right)
            
            return merge(left, right)
            
        return mergesort(head)
            

        