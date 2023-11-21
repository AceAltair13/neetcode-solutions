# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def traverse(node, d):
            nonlocal depth
            depth = max(depth, d)
            if node:
                traverse(node.left, d + 1)
                traverse(node.right, d + 1)
        
        traverse(root, depth)

        return depth