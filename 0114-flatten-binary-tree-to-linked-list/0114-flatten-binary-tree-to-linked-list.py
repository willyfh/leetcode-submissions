# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def helper(node):
            if node == None:
                return
            arr.append(node.val)
            helper(node.left)
            helper(node.right)
            
        helper(root)
        
        if root==None:
            return root
        
        root.left = None
        
        for i in range(len(arr)):
            if i==0:
                continue
            root.right = TreeNode(arr[i])
            root = root.right
            
            
        