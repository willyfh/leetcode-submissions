class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        
        self.helper(k, n, ans, [], 0, 0)
        
        return ans
        
    def helper(self, k, n, ans, temp, s, start_num):
        
        if k == len(temp):
            if s == n:
                ans.append(temp.copy())
            return
        
        for i in range(start_num+1, 10):
            temp.append(i)
            self.helper(k, n, ans, temp, s+i, i)
            temp.pop()