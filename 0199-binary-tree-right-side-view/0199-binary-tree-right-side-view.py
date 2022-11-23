# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        if root==None:
            return out
        
        q = deque()
        q.append((root, 0))
        prev = 0
        while len(q)>0:
            node, lvl = q.popleft()
            if lvl != prev:
                prev = lvl
                out.append(last.val)
            last = node
            if node.left != None:
                q.append((node.left, lvl+1))
            if node.right != None:
                q.append((node.right, lvl+1))   
        out.append(last.val)
        return out
        