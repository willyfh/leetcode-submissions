class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        ans = []
        def helper(arr, i):
            s = sum(arr)
            if s==target:
                ans.append([*arr])
            elif s>target:
                return
            
            for j in range(i, len(candidates)):
                c = candidates[j]
                arr.append(c)
                helper(arr, j)
                arr.pop()
        
        
        helper([], 0)
        
        return ans