"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node = head
        newHead = Node(0)
        newNode = newHead
        d = {}
        while node != None:
            if node not in d:
                temp = Node(node.val)
                newNode.next = temp
                d[node] = temp
            else:
                newNode.next = d[node]
                
            if node.random!=None and node.random not in d:
                temp = Node(node.random.val)
                newNode.next.random = temp
                d[node.random] = temp
            else:
                if node.random!=None:
                    newNode.next.random = d[node.random]
            newNode = newNode.next
            node = node.next
        return newHead.next
            
        
            
            
            