class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        out = []
        s = nums[0]
        e = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            prev_num = nums[i-1]
            if num - prev_num > 1 :
                if s==e:
                    out.append(str(s))
                else:
                    out.append(str(s) +"->" + str(e))
                    
                s = num
                e = num
                    
            else:
                e = num
                
        if s==e:
            out.append(str(s))
        else:
            out.append(str(s) +"->" + str(e))
            
        return out