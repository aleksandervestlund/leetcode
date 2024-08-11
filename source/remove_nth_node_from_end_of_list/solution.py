from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None
        length = 1
        start = head
        while (start := start.next) is not None:  # type: ignore
            length += 1
        if length == n:
            return head.next
        prev = None
        next_ = head
        for _ in range(length - n):
            prev = next_
            next_ = next_.next  # type: ignore
        print(prev, next_, length)
        if prev is None:
            return next_
        prev.next = next_.next  # type: ignore
        return head
