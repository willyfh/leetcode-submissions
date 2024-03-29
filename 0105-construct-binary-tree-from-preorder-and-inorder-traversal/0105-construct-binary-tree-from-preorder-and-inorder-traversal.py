# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(idx, left, right):
            if left > right:
                return None
            node = TreeNode()
            node.val = preorder[idx[0]]
            idx[0] +=1
            
            pivot = d[node.val] 
            
            node.left = helper(idx, left, pivot-1)
            node.right = helper(idx, pivot+1, right)
            
            
            return node
            
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i
            
        return helper([0], 0, len(inorder)-1)
        
        
        