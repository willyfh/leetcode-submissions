class StockSpanner:

    def __init__(self):
        self.d = deque()

    def next(self, price: int) -> int:
        ans = 1
        while self.d and price >= self.d[-1][0]:
            p, a =  self.d.pop()
            ans+=a
            
        self.d.append((price, ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)