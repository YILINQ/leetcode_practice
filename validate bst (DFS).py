# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        result = []
        current = root
        flag = True
        while flag:
            if current:
                stack.append(current)
                current = current.left
            elif stack != []:
                current = stack.pop()
                if result != []:
                    if current.val <= result[-1]:
                        return False
                result.append(current.val)
                current = current.right
            else:
                break
        return flag