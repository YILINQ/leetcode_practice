# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        inc_bit = 0
        result = ListNode(0)
        cur = result
        inc_bit = 0
        prev1 = l1
        prev2 = l2
        current_val = 0

        while prev1 or prev2:
            current_val = inc_bit
            if prev1:
                current_val += prev1.val
            if prev2:
                current_val += prev2.val

            inc_bit = current_val // 10
            current_val = current_val % 10

            cur.next = ListNode(current_val)
            cur = cur.next
            if prev1:
                prev1 = prev1.next
            if prev2:
                prev2 = prev2.next
        if inc_bit == 1:
            cur.next = ListNode(inc_bit)
        return result.next