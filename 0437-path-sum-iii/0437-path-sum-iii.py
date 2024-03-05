# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        self.d.append(root.val)
        paths, curr_sum = 0, sum(self.d)

        for i in range(len(self.d)):
            if curr_sum == targetSum:
                paths += 1

            curr_sum -= self.d[i]
        
        leftPaths = self.pathSum(root.left, targetSum)
        rightPaths = self.pathSum(root.right, targetSum)

        self.d.pop()
        return paths + leftPaths + rightPaths
    
    
