, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(
        self, root: Optional[TreeNode], path: Optional[list[int]] = None
    ) -> list[int]:
        if path is None:
            path = []
        if root is not None:
            self.inorderTraversal(root.left, path)
            path.append(root.val)
            self.inorderTraversal(root.right, path)
        return path
