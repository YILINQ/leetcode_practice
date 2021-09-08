"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root == []:
            return None
        root.next = None
        queue = [root]
        while queue != []:
            queue[-1].next = None
            n = len(queue)
            for i in range(n):
                if i != n - 1:
                    queue[0].next = queue[1]
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
        return root