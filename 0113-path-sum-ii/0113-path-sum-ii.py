# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def helper(node, tempList, remainingSum):
            if node is None:
                return False
            tempList.append(node.val)
            if node.left is None and node.right is None: #leaf
                if remainingSum == node.val:
                    ans.append(tempList.copy())
            
            left = helper(node.left, tempList, remainingSum-node.val)
            if node.left is not None:
                tempList.pop()

            right = helper(node.right, tempList, remainingSum-node.val)
            if node.right is not None:
                tempList.pop()
            
        helper(root, [], targetSum)

        return ans