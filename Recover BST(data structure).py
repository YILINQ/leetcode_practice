# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.first, self.second, self.pre = None, None, None

        def traverse(node):
            if not node: return
            traverse(node.left)
            if (self.pre and self.pre.val >= node.val):
                if not self.first: self.first = self.pre
                self.second = node
            self.pre = node
            traverse(node.right)

        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val