# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def traverse(node, largest):
            nonlocal good_nodes

            if node:
                if node.val >= largest:
                    good_nodes += 1
                    largest = max(largest, node.val)
                traverse(node.left, largest)
                traverse(node.right, largest)

        traverse(root, root.val)

        return good_nodes
