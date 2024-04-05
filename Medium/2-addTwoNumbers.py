class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next

# LeetCode 2