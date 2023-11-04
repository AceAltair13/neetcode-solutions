# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp_node = ListNode(0, head)
        prev_group = temp_node

        while True:
            k_group = self.get_kth_node(prev_group, k)
            if not k_group:
                break
            next_group = k_group.next

            prev, curr = k_group.next, prev_group.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp2 = prev_group.next
            prev_group.next = k_group
            prev_group = temp2

        return temp_node.next

    def get_kth_node(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head
