"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root ==None:
            return 0
        
        q = deque()
        q.append((root,1))
        
        ans = 0
        while len(q)>0:
            node, lvl = q.popleft()
            ans = max(ans, lvl)
            for c in node.children:
                q.append((c, lvl+1))
                
        return ans