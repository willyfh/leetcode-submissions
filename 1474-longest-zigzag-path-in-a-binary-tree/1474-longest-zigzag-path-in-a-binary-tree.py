# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        return max(self.helper(root.right, 'l', 0), self.helper(root.left, 'r', 0))
    def helper(self, node, d, s):
        if not node:
            return s
        if d == 'l':
            return max(self.helper(node.right, 'l', 0), self.helper(node.left, 'r', s+1))
        elif d == 'r':
            return max(self.helper(node.left, 'r', 0), self.helper(node.right, 'l', s+1))