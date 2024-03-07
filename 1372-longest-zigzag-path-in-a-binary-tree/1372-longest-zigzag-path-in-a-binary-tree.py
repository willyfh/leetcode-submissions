# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
       
        def helper(node, direction, currLength):
            if node == None:
                return
                        
            self.ans = max(self.ans, currLength)
            
            if direction=='r':
                helper(node.right, "l", currLength+1)
                helper(node.left, "r", 1)
            else:
                helper(node.left, "r", currLength+1)
                helper(node.right, "l", 1)
                
        
        if root == None:
            return 0
        
        helper(root.left, "r", 1)
        helper(root.right, "l", 1)
        
        return self.ans