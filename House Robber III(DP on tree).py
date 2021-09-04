# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def DFS(root):
            # lst[0]: use root
            # lst[1]: without root
            leaf = [root.val, 0]
            if root.left:
                temp = DFS(root.left)
                leaf[0] += temp[1]
                leaf[1] += max(temp)
            if root.right:
                temp = DFS(root.right)
                leaf[0] += temp[1]
                leaf[1] += max(temp)
            return leaf

        return max(DFS(root))
