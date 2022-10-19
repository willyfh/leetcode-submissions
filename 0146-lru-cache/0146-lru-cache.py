class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        else:
            node = self.m[key]
            self.remove(node)
            self.addToTail(node)
            return node.val
            
    def put(self, key: int, value: int) -> None:
            if key not in self.m:
                if len(self.m) >= self.capacity:
                    self.removeFromHead()
                node = LinkedList(key, value)
                self.addToTail(node)
                self.m[key] = node
            else:
                self.remove(self.m[key])
                self.m[key].val = value
                self.addToTail(self.m[key])

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def addToTail(self,node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        
    def removeFromHead(self):
        self.m.pop(self.head.next.key)
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)