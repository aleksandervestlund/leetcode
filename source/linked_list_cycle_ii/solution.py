from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        seen = {id(head)}
        while (next_ := head.next) is not None:  # type: ignore
            id_ = id(next_)
            if id_ in seen:
                return next_
            head = next_
            seen.add(id_)
        return None
