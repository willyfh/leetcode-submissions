# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        
        ans = 0
        max_level = float("-inf")
        q = deque()
        q.append(root)
        
        max_level_temp = 0
        num_level = 1
        next_level = 0
        idx_level = 1
        
        while len(q) > 0:
            curr = q.popleft()
            max_level_temp += curr.val
            num_level -= 1
            
            if curr.left:
                q.append(curr.left)
                next_level+=1
                
            if curr.right:
                q.append(curr.right)
                next_level+=1
                
            if num_level == 0:
                if max_level_temp > max_level:
                    max_level = max_level_temp
                    ans = idx_level
                idx_level += 1
                max_level_temp = 0
                num_level = next_level
                next_level = 0
                    
        return ans