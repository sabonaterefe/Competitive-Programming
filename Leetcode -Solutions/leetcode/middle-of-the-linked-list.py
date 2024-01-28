from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        length = 0
        while runner:
            length += 1
            runner = runner.next

        for _ in range(length // 2):
            head = head.next

        return head