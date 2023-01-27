class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = LinkedList(0,0)
        self.tail = LinkedList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, k: int) -> int:
        if k in self.data:
            
            if self.data[k].next != None:
                self.data[k].next.prev = self.data[k].prev
            if self.data[k].prev != None:
                self.data[k].prev.next = self.data[k].next
                
            self.data[k].next = None
            self.data[k].prev = None
            
            self.data[k].next = self.head.next
            self.data[k].prev = self.head
            
            self.head.next.prev = self.data[k]
            
            self.head.next = self.data[k]
            
            return self.data[k].val
        else:
            return -1

    def put(self, k: int, value: int) -> None:
        if k in self.data:
            
            self.data[k].val = value
            
            if self.data[k].next != None:
                self.data[k].next.prev = self.data[k].prev
            if self.data[k].prev != None:
                self.data[k].prev.next = self.data[k].next
                
            self.data[k].next = None
            self.data[k].prev = None
            
            self.data[k].next = self.head.next
            self.data[k].prev = self.head
            self.head.next.prev = self.data[k]
            self.head.next = self.data[k]
            
        else:
            if len(self.data)<self.capacity:
                node = LinkedList(k, value)
                node.next = self.head.next
                node.prev = self.head
                
                self.head.next.prev = node
                self.head.next = node
                
                self.data[k] = node
            else:
                node = LinkedList(k, value)
                
                node.next = self.head.next
                node.prev = self.head
                
                self.head.next.prev = node
                self.head.next = node
                
                self.data[k] = node
                self.data.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)