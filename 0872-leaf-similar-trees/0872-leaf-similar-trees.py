# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        arr1 = []
        arr2 = []
        
        def collect_leaf(node, arr):
            if node.left == None and node.right == None:
                arr.append(node.val)
                
            if node.left != None:
                collect_leaf(node.left, arr)
                
            if node.right != None:
                collect_leaf(node.right, arr)
                
        collect_leaf(root1, arr1)
        
        collect_leaf(root2, arr2)
        
        return arr1 == arr2