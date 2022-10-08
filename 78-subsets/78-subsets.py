class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, ans, temp):
            for k in range(i, len(nums)):
                temp.append(nums[k])
                ans.append([*temp])
                helper(k+1, nums, ans, temp)
                temp.pop()
        ans = [[]]
        helper(0, nums, ans, [])
        return ans
                