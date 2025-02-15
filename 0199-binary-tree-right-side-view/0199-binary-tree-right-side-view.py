# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        row = 1
        ans = []
        next_row = 0
        while len(q)>0:
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
                next_row += 1
            if node.right is not None:
                q.append(node.right)
                next_row += 1
            row-=1
            if row == 0:
                ans.append(node.val)
                row = next_row
                next_row=0
        return ans


