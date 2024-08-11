# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode], path: Optional[List[int]] = None) -> List[int]:
        if path is None:
            path = []
        if root is not None:
            self.postorderTraversal(root.left, path)
            self.postorderTraversal(root.right, path)
            path.append(root.val)
        return path
