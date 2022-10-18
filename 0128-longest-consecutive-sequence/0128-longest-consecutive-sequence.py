class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        v = {}
        
        for i in range(len(nums)):
            d[nums[i]] = i
            v[nums[i]] = False
            
        
        ans = 0
        for i in range(len(nums)):

            if v[nums[i]] == False:
                temp = 1 
                v[nums[i]] = True
                j = i
                while nums[j]+1 in d:
                    temp += 1
                    v[nums[j]+1] = True
                    j = d[nums[j]+1]
                j = i
                while nums[j]-1 in d:
                    temp+=1
                    v[nums[j]-1] = True
                    j = d[nums[j]-1]
                ans = max(ans, temp)
                
        return ans