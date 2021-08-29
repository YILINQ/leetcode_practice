# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head is None or head.next is None):
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if fast is None or fast.next is None:
                # end
                return False
            slow = slow.next
            fast = fast.next.next
        return True