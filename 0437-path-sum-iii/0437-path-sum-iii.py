# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.ans = 0
        
        cache = {0: 1}
             
        def pathSumHelper(node, currSum):
            if node == None:
                return
            currSum += node.val
            
            oldSum = currSum - targetSum
            
            if oldSum in cache:
                self.ans += cache[oldSum]
                
            if currSum not in cache:
                cache[currSum] = 1
            else:
                cache[currSum] += 1
                
            pathSumHelper(node.left, currSum)
            pathSumHelper(node.right, currSum)

            cache[currSum] -= 1

            
        pathSumHelper(root, 0)
        return self.ans