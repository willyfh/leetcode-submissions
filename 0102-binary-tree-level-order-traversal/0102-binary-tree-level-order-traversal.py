# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root ==None:
            return []
        
        ans = []
        temp = []
        q = deque()
        q.append((root, 0))
        
        i=0
        while len(q)>0:
            curr = q.popleft()
            if curr[1]==i:
                temp.append(curr[0].val)
            else:
                ans.append([*temp])
                i+=1
                temp = [curr[0].val]
            
            if curr[0].left !=None:
                q.append((curr[0].left, i+1))
            if curr[0].right!=None:
                q.append((curr[0].right, i+1))
        
        
        ans.append([*temp])
        return ans
            