class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        
        
        s = {}
        visited = set()
        
        for i in range(len(nums)):
            s[nums[i]] = i
        
        ans = 1
        c = 1
        visited.add(nums[0])
        for i in range(len(nums)):
            k=i
            while nums[k]+1 in s and nums[k]+1 not in visited:
                c+=1
                visited.add(nums[k]+1)
                k = s[nums[k]+1]
            k=i
            while nums[k]-1 in s and nums[k]-1 not in visited:
                c+=1
                visited.add(nums[k]-1)
                k = s[nums[k]-1]
            ans = max(ans, c)
            c = 1
        return ans