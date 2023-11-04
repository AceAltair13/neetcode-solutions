# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            updatedLists = []
            for i in range(0, len(lists), 2):
                _list1 = lists[i]
                _list2 = lists[i + 1] if (i + 1) < len(lists) else None
                updatedLists.append(self.merge2Lists(_list1, _list2))
            lists = updatedLists
        return lists[0]

    def merge2Lists(self, list1, list2):
        _head = ListNode()
        curr = _head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return _head.next
