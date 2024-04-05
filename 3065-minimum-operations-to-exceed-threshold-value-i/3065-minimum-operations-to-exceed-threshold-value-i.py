class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for num in nums:
            if num<k:
                ans+=1
            else:
                break
        return ans