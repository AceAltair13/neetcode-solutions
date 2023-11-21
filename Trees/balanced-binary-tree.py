# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def traverse(node):
            if not node:
                return 0, True
            left_depth, left_check = traverse(node.left)
            right_depth, right_check = traverse(node.right)
            diff = abs(left_depth - right_depth)
            check = left_check and right_check and diff <= 1

            return 1 + max(left_depth, right_depth), check
        
        return traverse(root)[1]
            