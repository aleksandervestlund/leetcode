from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(
        self, root: Optional[TreeNode], path: Optional[list[int]] = None
    ) -> list[int]:
        if path is None:
            path = []
        if root is not None:
            path.append(root.val)
            self.preorderTraversal(root.left, path)
            self.preorderTraversal(root.right, path)
        return path
