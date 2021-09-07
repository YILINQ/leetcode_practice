# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == [] or root is None:
            return []

        result = [[root.val]]
        queue = [root]
        current_level = []
        while queue != []:
            current_level = []
            for i in range(len(queue)):
                if queue[0].left:
                    current_level.append(queue[0].left.val)
                    queue.append(queue[0].left)
                if queue[0].right:
                    current_level.append(queue[0].right.val)
                    queue.append(queue[0].right)
                queue.pop(0)
            if current_level != []:
                result.append(current_level)

        return result[::-1]

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == [] or root is None:
            return []

        result = [[root.val]]
        queue = [root]
        current_level = []
        while queue != []:
            current_level = []
            for i in range(len(queue)):
                if queue[0].left:
                    current_level.append(queue[0].left.val)
                    queue.append(queue[0].left)
                if queue[0].right:
                    current_level.append(queue[0].right.val)
                    queue.append(queue[0].right)
                queue.pop(0)
            if current_level != []:
                result.append(current_level)

        if len(result) >= 1:
            for i in range(1, len(result), 2):
                result[i] = result[i][::-1]
        return result