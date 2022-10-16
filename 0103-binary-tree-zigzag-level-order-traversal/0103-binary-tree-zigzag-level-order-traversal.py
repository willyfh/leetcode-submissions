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
        
        toright = True
        i=1
        j =0
        
        ans = []
        temp = []
        
        while len(q)>0:
            if toright:
                curr = q.popleft()
                temp.append(curr.val)
                i-=1
                
                if curr.left != None:
                    q.append(curr.left)
                    j+=1
                
                if curr.right != None:
                    q.append(curr.right)
                    j+=1
                    
                if i==0:
                    toright=False
                    ans.append([*temp])
                    temp = []
                    i=j
                    j=0
                    
            else:
                curr = q.pop()
                temp.append(curr.val)
                i-=1
                
                if curr.right != None:
                    q.appendleft(curr.right)
                    j+=1
                    
                if curr.left != None:
                    q.appendleft(curr.left)
                    j+=1
                    
                if i == 0:
                    toright = True
                    ans.append([*temp])
                    temp = []
                    i = j
                    j=0
                    
                    
        return ans
                
                