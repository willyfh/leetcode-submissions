class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        s=0
        for num in nums:
            s+=num
            ans.append(s)
        return ans