# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        m = 0
        cur = head
        while cur:
            m += 1
            cur = cur.next

        if m < n:
            return None
        if m == n:
            return head.next
        prev = head
        cur = prev.next
        count = 1
        while prev:
            if count == m - n:
                cur = cur.next
                prev.next = cur
            prev = cur
            if not prev:
                break
            cur = cur.next
            count += 1
        return head