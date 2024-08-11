from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        seen = {id(headA)}
        while (next_ := headA.next) is not None:
            seen.add(id(next_))
            headA = next_
        if id(headB) in seen:
            return headB
        while (next_ := headB.next) is not None:
            if id(next_) in seen:
                return next_
            headB = next_
        return None
