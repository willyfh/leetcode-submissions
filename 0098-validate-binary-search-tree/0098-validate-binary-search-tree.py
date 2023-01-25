# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(tree, mi, ma):
            if tree == None:
                return True
            
            if tree.val <= mi or tree.val >= ma:
                return False
            
            a = True
            if tree.left !=None:
                a = helper(tree.left, mi, tree.val)
                
            b = True
            if tree.right!=None:
                b = helper(tree.right, tree.val, ma)
                
            return a and b
            
        return helper(root, -sys.maxsize-1, sys.maxsize)