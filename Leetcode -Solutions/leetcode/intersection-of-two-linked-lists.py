# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA= headA
        currB = headB
        nodeA = headA
        nodeB = headB
        sizeA=0
        sizeB=0
        while currA:
            sizeA+=1
            currA=currA.next
        while currB:
            sizeB+=1
            currB=currB.next
        if sizeA>sizeB:
            for _ in range(sizeA-sizeB):
                nodeA=nodeA.next
        else:
            for _ in range(sizeB-sizeA):
                nodeB = nodeB.next
        while nodeA!=nodeB:
            nodeA=nodeA.next
            nodeB=nodeB.next
        return nodeA
          

                
        
            

        
        
        
        
        
            
        



        