# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root == None:
            return None
        
        if root.val ==key:
            temp = root.right
            prev = temp
            if temp:
                while temp.left:
                    prev = temp
                    temp = temp.left
                prev.left= None
            if not temp:
                return root.left
            else:
                
                temp.left = root.left
                root.left = None
                
                if temp == root.right:
                    return temp
                if temp.right is None:
                    temp.right = root.right
                    return temp

                temp2 = temp.right
                while temp2.right:
                
                    temp2 = temp2.right
                temp2.right = root.right
                return temp
            
        left, right = root.left, root.right
        if key < root.val:
            left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            right = self.deleteNode(root.right, key)
            
        root.left = left
        root.right = right
        
        return root
            
        
            