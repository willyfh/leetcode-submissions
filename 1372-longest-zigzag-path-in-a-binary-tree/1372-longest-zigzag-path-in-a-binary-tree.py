# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        if root == None:
            return 0
        
        self.helper(root.left, "r", 0)
        self.helper(root.right, "l", 0)
        
        return self.ans
    
    def helper(self, node, direction, currLength):
        
        if node == None:
            return
        
        currLength += 1
        
        self.ans = max(self.ans, currLength)

        if direction=='r':
            self.helper(node.right, "l", currLength)
            self.helper(node.left, "r", 0)
        else:
            self.helper(node.left, "r", currLength)
            self.helper(node.right, "l", 0)