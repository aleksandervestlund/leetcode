from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        idx = 0
        total = 0
        changed = True

        while changed:
            first = 0 if l1 is None else l1.val
            second = 0 if l2 is None else l2.val
            total += (first + second) * 10**idx
            idx += 1

            changed = False

            if l1 is not None:
                l1 = l1.next
                changed = True
            if l2 is not None:
                l2 = l2.next
                changed = True

        totall = reversed(str(total))
        firstt = ListNode(int(next(totall)))
        prev = firstt

        for item in totall:
            new = ListNode(int(item))
            prev.next = new
            prev = new

        return firstt
