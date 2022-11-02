# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if node == None:
                return None
            
            left = helper(node.left)
            right = helper(node.right)
            
            if (left == p or left == q) and (right == p or right == q):
                return node
            elif (node == p and (left == q or right == q)) or (node == q and (left == 1 or right == q)):
                return node
            elif node == p or node == q:
                return node
            elif left !=None:
                return left
            elif right !=None:
                return right
            return None
        
        return helper(root)
                