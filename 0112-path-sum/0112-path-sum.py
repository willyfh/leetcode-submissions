# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, currSum):
            if node is None:
                return False
            currSum += node.val
            if node.left is None and node.right is None:
                if currSum == targetSum:
                    return True
            return helper(node.left, currSum) or helper(node.right, currSum)
                

        if root is None:
            return False
        return helper(root, 0)