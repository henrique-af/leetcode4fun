# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, curr = head, head.next
        idx = 1
        critical_points = []

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (
                curr.val < prev.val and curr.val < curr.next.val
            ):
                critical_points.append(idx)
            prev = curr
            curr = curr.next
            idx += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float("inf")
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(
                min_distance, critical_points[i] - critical_points[i - 1]
            )

        return [min_distance, max_distance]
