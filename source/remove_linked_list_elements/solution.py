from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        prev = head
        while (next_ := prev.next) is not None:
            if next_.val == val:
                prev.next = next_.next
            else:
                prev = next_
        return head
