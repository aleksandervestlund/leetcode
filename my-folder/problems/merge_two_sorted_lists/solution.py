# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            head = list1
            first = list1.next
            second = list2
        else:
            head = list2
            first = list1
            second = list2.next

        prev = head
        while True:
            if first is None:
                prev.next = second
                break
            if second is None:
                prev.next = first
                break
            if first.val < second.val:
                prev.next = first
                prev = first
                first = first.next
            else:
                prev.next = second
                prev = second
                second = second.next
        
        return head
