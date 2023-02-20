# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        
        nodeA = headA
        while nodeA!=None:
            s.add(nodeA)
            nodeA = nodeA.next
            
        nodeB = headB
        while nodeB!=None:
            if nodeB in s:
                return nodeB
            nodeB = nodeB.next
            
        return None