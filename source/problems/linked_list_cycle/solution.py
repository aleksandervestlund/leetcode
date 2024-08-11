# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = {id(head)}
        while (next_ := head.next) is not None:
            head = next_
            id_ = id(head)
            if id_ in seen:
                return True
            seen.add(id_)
        return False
