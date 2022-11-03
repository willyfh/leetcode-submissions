# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # Since we know input node is not last node, so nextNode will not be null
        nextNode = node.next
        # Step 2
        node.val = nextNode.val
        # Step 3
        node.next = nextNode.next
        nextNode.next = None