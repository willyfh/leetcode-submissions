# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, is_left):
            if node == None:
                return 0
            if node.left == None and node.right == None: #leaf
                if is_left:
                    return node.val
                else:
                    return 0
            return helper(node.left, True) + helper(node.right, False)
        return helper(root, False)