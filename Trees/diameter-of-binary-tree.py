# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def traverse(node):
            nonlocal dia

            if not node:
                return 0
            else:
                left = traverse(node.left)
                right = traverse(node.right)
                dia = max(dia, left + right)

            return 1 + max(left, right)

        traverse(root)

        return dia
