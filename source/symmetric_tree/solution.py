from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        if root is None:
            return True
        return isSameTree(root.left, root.right)
