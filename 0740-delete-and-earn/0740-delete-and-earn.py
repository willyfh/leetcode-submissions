class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
                
            d[nums[i]] += nums[i]
        
        keys = [k[0] for k in sorted(d.items(), key=lambda x: x[0])]
        dp = [0]*len(keys)
        dp[0] = d[keys[0]]
        if len(keys)==1:
            return d[keys[0]]
        if keys[0]+1 == keys[1]:
            dp[1] = max(d[keys[0]], d[keys[1]])
        else:
            dp[1] = d[keys[0]] + d[keys[1]]
        if len(keys)==2:
            return dp[1]
        for i in range(2, len(keys)):
            if keys[i]-1 == keys[i-1]:
                dp[i] = max(d[keys[i]] + dp[i-2], dp[i-1])
            else:
                dp[i] = max(d[keys[i]] + dp[i-2], d[keys[i]]+dp[i-1])
        
        return dp[-1]