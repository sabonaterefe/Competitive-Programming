class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddHead = head
        oddTail = None
        evenHead = head.next
        evenTail = None

        index = 1
        curr = head

        while curr:
            if index % 2 == 1:  
                if oddTail is None:
                    oddTail = curr
                else:
                    oddTail.next = curr
                    oddTail = oddTail.next
            else: 
                if evenTail is None:
                    evenTail = curr
                else:
                    evenTail.next = curr
                    evenTail = evenTail.next

            curr = curr.next
            index += 1

        if oddTail is None:
            return evenHead

        oddTail.next = evenHead

        if evenTail is not None:
            evenTail.next = None

        return oddHead