# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        max_level = -1
        q = collections.deque([root])
        level = 0
        while len(q)>0:
            size = len(q)
            curr_sum = 0
            level += 1
            for i in range(size):
                node = q.popleft()
                curr_sum += node.val
                if i == size - 1:
                    
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                        max_level = level
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return max_level