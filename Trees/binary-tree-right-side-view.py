# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)

        level_order_tree = [[] for _ in range(height)]

        def level_order(node, level):
            if node:
                level_order_tree[level].append(node.val)
                level_order(node.left, level + 1)
                level_order(node.right, level + 1)

        level_order(root, 0)

        ret = []

        for level in level_order_tree:
            ret.append(level[-1])

        return ret
