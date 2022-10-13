# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        def helper(node):
            
            if node.left == None and node.right == None:
                return 0
        
            if node.left ==None:
                return helper(node.right) + 1
            
            if node.right == None:
                return helper(node.left) + 1
            
            left = helper(node.left)
            right = helper(node.right)
            
            return min(left, right) + 1
        
        return helper(root) + 1