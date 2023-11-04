"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        ptr_dict = {None: None}
        curr = head

        while curr:
            _curr = Node(curr.val)
            ptr_dict[curr] = _curr
            curr = curr.next

        curr = head

        while curr:
            _curr = ptr_dict[curr]
            _curr.next = ptr_dict[curr.next]
            _curr.random = ptr_dict[curr.random]
            curr = curr.next

        return ptr_dict[head]
