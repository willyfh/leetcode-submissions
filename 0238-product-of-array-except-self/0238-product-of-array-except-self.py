class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [1]*len(nums)
        suf = [1]*len(nums)
        
        i=1
        j=len(nums)-2
        

        while i<len(nums):
            pref[i] = pref[i-1]*nums[i-1]
            suf[j] = suf[j+1]*nums[j+1]
            i+=1
            j-=1
        
        ans = []
        for i in range(len(nums)):
            ans.append(pref[i] * suf[i])
            
        return ans
            
        
        