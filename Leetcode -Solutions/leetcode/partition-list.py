class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller_head = smaller_tail = ListNode(0)
        greater_head = greater_tail = ListNode(0)

        curr = head
        while curr:
            if curr.val < x:
                smaller_tail.next = curr
                smaller_tail = curr
            else:
                greater_tail.next = curr
                greater_tail = curr
            curr = curr.next

        smaller_tail.next = greater_head.next
        greater_tail.next = None

        return smaller_head.next