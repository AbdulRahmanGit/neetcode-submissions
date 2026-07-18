# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        walker, runner = head, head.next
        while runner and runner.next:
            walker =  walker.next
            runner = runner.next.next
        #now we have to reverse the second part of the ll
        second = walker.next
        prev = walker.next = None
        while second:
            temp = second.next
            second.next = prev 
            prev = second
            second = temp
        # now merging both the side
        first,second = head, prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2  
