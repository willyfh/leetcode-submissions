# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0
        
        def good_nodes(node, max_val):
            nonlocal ans
            if node == None:
                return
            if node.val >= max_val:
                ans += 1
            good_nodes(node.left, max(max_val, node.val))
            good_nodes(node.right, max(max_val, node.val))
            
        good_nodes(root, float('-inf'))
        
        return ans