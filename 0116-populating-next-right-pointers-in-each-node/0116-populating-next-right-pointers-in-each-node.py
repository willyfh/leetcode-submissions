"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':        
        def helper(node):
            if node == None:
                return
    
            if node.left!=None:
                node.left.next = node.right
                
            if node.right!=None and node.next!=None:
                node.right.next = node.next.left
                
            helper(node.left)
            helper(node.right)
                        
        helper(root)
        return root
            