"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.seen = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        if head in self.seen:
            return self.seen[head]
        copy = Node(head.val)
        self.seen[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.seen.get(head.random)
        return copy