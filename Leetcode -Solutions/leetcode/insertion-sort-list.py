class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        sorted_tail = head
        curr = head.next
        
        while curr:
            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
            else:
                sorted_tail.next = curr.next
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                
            
                curr.next = prev.next
                prev.next = curr
                curr = sorted_tail.next
        
        return dummy.next