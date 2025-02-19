# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
        def helper(node, depth):
            if node is None:
                return
            self.max = max(self.max, depth)
            depth += 1
            helper(node.left, depth)
            helper(node.right, depth)
        
        if root is None:
            return 0
        helper(root, 1)
        return self.max
            