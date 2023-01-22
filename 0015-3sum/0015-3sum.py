class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for k in range(len(nums)):
            d[nums[k]*-1] = k
            
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k_val = nums[i]+nums[j]
                if nums[i]+nums[j] in d:
                    if i!=d[k_val] and j!=d[k_val]:
                        ans.add(str(sorted([nums[i], nums[j], k_val*-1])))
        return [eval(a) for a in ans]