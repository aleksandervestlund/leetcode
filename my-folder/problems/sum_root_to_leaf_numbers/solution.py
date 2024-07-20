# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return int(root.val)
        root.val = str(root.val)
        if root.left is not None:
            root.left.val = root.val + str(root.left.val)
        if root.right is not None:
            root.right.val = root.val + str(root.right.val)
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)
