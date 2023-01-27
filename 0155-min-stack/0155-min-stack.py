class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        mi = val
        if len(self.stack)>0:
            mi = min(self.stack[-1][1], val)
        self.stack.append((val, mi))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()