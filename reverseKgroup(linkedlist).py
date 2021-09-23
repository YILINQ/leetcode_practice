# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # dummy node
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return dummy.next
            next_next = tail.next
            head, tail = self.reverse(head, tail)

            # connect back
            pre.next = head
            tail.next = next_next
            pre = tail
            head = tail.next
        return dummy.next

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            next_next = p.next
            p.next = prev
            prev = p
            p = next_next
        return tail, head