# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ret = False

        def scan_tree(node):
            nonlocal ret

            if node and subRoot and node.val == subRoot.val:
                ret = check(node, subRoot)
            elif node and not subRoot:
                return True
            elif not node and subRoot:
                return False
            
            return ret or scan_tree(node.left) or scan_tree(node.right)

        def check(node, subnode):
            if not node and not subnode:
                return True
            if node and not subnode:
                return False
            if not node and subnode:
                return False
            if node.val == subnode.val:
                return True and check(node.left, subnode.left) and check(node.right, subnode.right)

        scan_tree(root)

        return ret            