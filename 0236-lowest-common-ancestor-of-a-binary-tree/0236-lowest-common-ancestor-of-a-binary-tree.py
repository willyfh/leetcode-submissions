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
            
            if (left != None) and (right != None):
                return node
            elif node == p or node == q:
                return node
            elif left !=None:
                return left
            elif right !=None:
                return right
            return None
        
        return helper(root)
                