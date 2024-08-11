from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val  # type: ignore
        node.next = node.next.next  # type: ignore
