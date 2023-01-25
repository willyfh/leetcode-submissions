# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        q = deque()
        q.append((root,0))
        ans = []
        lvl_nodes = []
        curr_level = 0
        while len(q) > 0:
            curr, lvl = q.popleft()
            if lvl!=curr_level:
                ans.append([*lvl_nodes])
                lvl_nodes = []
            curr_level=lvl
            lvl_nodes.append(curr.val)
            if curr.left != None:
                q.append((curr.left, lvl+1))
            if curr.right != None:
                q.append((curr.right, lvl+1))
        ans.append([*lvl_nodes])
                
        return ans
                