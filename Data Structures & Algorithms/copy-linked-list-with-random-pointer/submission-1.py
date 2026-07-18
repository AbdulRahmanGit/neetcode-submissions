"""
# Definition for a Node.
"""

    

class Solution:
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = defaultdict(lambda: Node(0))
        oldtocopy[None] = None

        curr = head
        while curr:
            oldtocopy[curr].val = curr.val
            oldtocopy[curr].next = oldtocopy[curr.next]
            oldtocopy[curr].random = oldtocopy[curr.random]
            curr = curr.next
        return oldtocopy[head]        