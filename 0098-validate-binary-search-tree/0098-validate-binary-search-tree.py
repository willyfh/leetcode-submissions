# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, mi, ma):
            if node == None:
                return True
            if node.val <= mi:
                return False
            if node.val >= ma:
                return False
            
            a = True
            if node.left!=None:
                a = helper(node.left, mi, node.val)
            b = True
            if node.right!=None:
                b = helper(node.right, node.val, ma)
                
            return a and b
        return helper(root, float("-inf"), float("inf"))