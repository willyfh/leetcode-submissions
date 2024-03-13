class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1, 1001)]
        self.s = set(self.h)

        

    def popSmallest(self) -> int:
        smallest = heappop(self.h)
        self.s.remove(smallest)
        return smallest
        

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)
            heappush(self.h, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)