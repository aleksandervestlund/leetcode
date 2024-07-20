# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        print(root)
        if root is None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        if root.left is not None:
            root.left.val += root.val
        if root.right is not None:
            root.right.val += root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
