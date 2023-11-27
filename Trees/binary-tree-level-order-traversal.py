# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)

        ret = [[] for _ in range(height)]

        def traverse(node, level):
            if node:
                ret[level].append(node.val)
                traverse(node.left, level + 1)
                traverse(node.right, level + 1)

        traverse(root, 0)

        return ret
