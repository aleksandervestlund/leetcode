# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head

        while curr is not None and (next_ := curr.next) is not None:
            if next_.val == curr.val:
                curr.next = next_.next
            else:
                curr = next_
        
        return head