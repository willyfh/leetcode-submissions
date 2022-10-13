# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, m):
            if node == None:
                return 0
            
            left = 1 + helper(node.left, m)
            right = 1 + helper(node.right, m)
            
            m[0] = max(m[0], abs(left-right))
            
            return max(left, right)
            
        m = [0]
        helper(root, m)
        
        if m[0] > 1:
            return False
        return True