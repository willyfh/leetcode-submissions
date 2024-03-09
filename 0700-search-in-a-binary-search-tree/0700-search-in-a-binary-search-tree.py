# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        
        left, right = None, None
        if root.left and val < root.val:
            left = self.searchBST(root.left, val)
            
        if root.right and val>=root.val:
            right = self.searchBST(root.right, val)
            
        return left if left else right