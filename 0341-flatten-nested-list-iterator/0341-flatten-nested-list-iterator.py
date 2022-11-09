# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ret = None
        self.nestedList = deque(nestedList)
    
    def next(self) -> int:
        return self.nestedList.popleft().getInteger()
        
    def hasNext(self) -> bool:
        while len(self.nestedList)!=0 and not self.nestedList[0].isInteger():
            p = self.nestedList.popleft()
            l = p.getList()
            for i in range(len(l)-1, -1, -1):
                self.nestedList.appendleft(l[i])
            if len(self.nestedList)==0:
                return False
        return len(self.nestedList)!=0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())