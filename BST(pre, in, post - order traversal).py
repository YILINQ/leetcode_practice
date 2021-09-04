# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack != []:
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                break
        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        visited = set()
        current = root
        while current and current not in visited:
            if current.left and current.left not in visited:
                current = current.left

            elif current.right and current.right not in visited:
                current = current.right

            else:
                result.append(current.val)
                visited.add(current)
                current = root
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root
        stack = []
        while True:
            if current:
                stack.append(current)
                result.append(current.val)
                current = current.left
            elif stack != []:
                current = stack.pop()
                current = current.right
            else:
                break
        return result