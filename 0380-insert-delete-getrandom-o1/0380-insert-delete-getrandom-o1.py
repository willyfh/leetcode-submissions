class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.arr.append(val) # store the value in arr, this helps to retrieve the element randomly by index
            self.s[val]=len(self.arr)-1 # store the index of val in the arr
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.s:
            idx = self.s[val]
            lastval = self.arr[-1]
            self.arr[idx] = lastval # this will remove the val at idx location, and move the last val here
            self.arr.pop() # then we can safely remove the val at the last idx since it was already moved before
            self.s[lastval] = idx # make sure to set the lastval to the new idx
            del self.s[val] # now we can remove the val from the dictionary
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()