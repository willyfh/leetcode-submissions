class Solution:

    def __init__(self, nums: List[int]):
        self.init_nums = [*nums]
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = [*self.init_nums]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()