# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        length = 1
        start = head
        while (start := start.next) is not None:
            length += 1
        if length == n:
            return head.next
        prev = None
        next_ = head
        for _ in range(length - n):
            prev = next_
            next_ = next_.next
        print(prev, next_, length)
        if prev is None:
            return next_
        prev.next = next_.next
        return head