class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = collections.deque()
        for i, num in enumerate(nums):
            if num !=0:
                if len(zeros)==0:
                    continue
                j = zeros.popleft()
                nums[j], nums[i] = nums[i], nums[j]
                zeros.append(i)
            else:
                zeros.append(i)