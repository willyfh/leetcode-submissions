# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans = [0]
        
        def pathSumHelper(node, target):
            
            if node == None:
                return
            
            computeAns(node, target)
                
            pathSumHelper(node.left, target)
            pathSumHelper(node.right, target)
            
        def computeAns(node, target):
            if node == None:
                return
            if node.val == target:
                ans[0] += 1
                
            computeAns(node.left, target-node.val)
            computeAns(node.right, target-node.val)
            
        
        pathSumHelper(root, targetSum)
        return ans[0]