class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        dp = {}
        def helper(start, temp):
            if start == len(s):
                ans.append(temp)
            for end in range(start+1, len(s)+1):
                st = s[start:end]

                if st in dp or st == st[::-1]:
                    dp[st] = True
                    temp.append(st)
                    helper(end, [*temp])
                    temp.pop()
        helper(0, [])       
        return ans