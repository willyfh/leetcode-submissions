# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def helper(node, p):
            
            if node == None:
                return
            p.append(node.val)
            if node.left == None and node.right == None:
                ans.append([*p])
                return
            if node.left:
                helper(node.left, p)
                p.pop()
            if node.right:
                helper(node.right, p)
                p.pop()
        helper(root, [])
        
            
        return ["->".join(map(str,a)) for a in ans]
            
            