class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        h = {}
        
        for i in range(len(nums)):
            
            if nums[i] not in h:
                h[nums[i]] = 0
            h[nums[i]] += 1
            
        c = 0
        for n in nums:
            if k-n in h and h[k-n]>0 and h[n]>0:
                if k-n!=n:
                    c+=1
                    h[n]-= 1
                    h[k-n]-=1
                else:
                    if h[n]>1:
                        c+=1
                        h[n]-= 2
                        
        return c