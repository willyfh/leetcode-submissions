# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def helper(node, s):
            if node.left==None and node.right==None:
                if targetSum == s:
                    return True
            
            if node.left != None:
                if helper(node.left, s+node.left.val):
                    return True
                
            if node.right != None:
                if helper(node.right, s+node.right.val):
                    return True
                
            return False
            
        if root == None:
            return False
        
        return helper(root, root.val)