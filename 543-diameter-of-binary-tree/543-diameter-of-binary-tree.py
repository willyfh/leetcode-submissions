# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, m):
            
            left = 0
            if node.left != None:
                left = 1 + helper(node.left, m)
            
            right = 0
            if node.right != None:
                right = 1 + helper(node.right, m)
              
            if left + right > m[0]:
                m[0] = left + right
            
            return max(left, right)
        
        m=[0]
        helper(root,m)
        return m[0]
            
            
            