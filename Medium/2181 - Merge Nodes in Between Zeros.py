# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        sum_nodes = 0
        dummy = ListNode(0)
        result = dummy

        while current:
            if current.val != 0:
                sum_nodes += current.val
            else:
                result.next = ListNode(sum_nodes)
                result = result.next
                sum_nodes = 0
            current = current.next

        return dummy.next
