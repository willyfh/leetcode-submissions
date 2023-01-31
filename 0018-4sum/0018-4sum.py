class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        d1 = {}
        t = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j]
                key = str(sorted([nums[i], nums[j]]))
                if key in t:
                    continue
                t.add(key)
                if k not in d1:
                    d1[k] = []
                d1[k].append([i, j])
                
        ans = []
        s = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j] - target
                if -k in d1:
                    for m in d1[-k]:
                        if i not in m and j not in m:
                            key = str(sorted([nums[i], nums[j], nums[m[0]], nums[m[1]]]))
                            if key not in s:
                                ans.append([nums[i], nums[j], nums[m[0]], nums[m[1]]])
                                s.add(key)
                            
        return ans