# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        q = deque()
        q.append(root)
        
        right_dir = True
        ans = []
        sublist=[]
        while len(q)>0:
            q_size = len(q)
            if right_dir:
                for i in range(q_size):
                    curr = q.popleft()
                    sublist.append(curr.val)
                    if curr.left!=None:
                        q.append(curr.left)
                    if curr.right!=None:
                        q.append(curr.right)
                right_dir = False
            else:
                for i in range(q_size):
                    curr = q.pop()
                    sublist.append(curr.val)
                    if curr.right!=None:
                        q.appendleft(curr.right)
                    if curr.left!=None:
                        q.appendleft(curr.left)
                        
                right_dir = True
            ans.append([*sublist])
            sublist = []
        return ans
                
                