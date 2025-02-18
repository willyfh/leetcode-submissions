# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]

        def helper(node, targetSum):
            if node is None:
                return

            findSum(node, targetSum)
            
            helper(node.left, targetSum)
            helper(node.right, targetSum)

        def findSum(node, currentSum):
            if node is None:
                return
            if node.val == currentSum:
                ans[0] += 1
            
            findSum(node.left, currentSum-node.val)
            findSum(node.right, currentSum-node.val)

        helper(root, targetSum)
        return ans[0]