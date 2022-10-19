class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.d = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        else:
            del self.d[self.d.index(key)]
            self.d.append(key)
            return self.m[key]
        
    def put(self, key: int, value: int) -> None:
            if key not in self.m:
                if len(self.m) >= self.capacity:
                    temp = self.d.popleft()
                    self.m.pop(temp)
                self.d.append(key)
                self.m[key] = value
            else:
                del self.d[self.d.index(key)]
                self.d.append(key)
                self.m[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)