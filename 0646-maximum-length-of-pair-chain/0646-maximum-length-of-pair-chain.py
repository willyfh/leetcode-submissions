class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        sorted_p = sorted(pairs, key=lambda x: x[1])
        
        s = sorted_p[0]
        ans = 1
        for i in range(1, len(sorted_p)):
            if sorted_p[i][0] > s[1]:
                ans += 1
                s = sorted_p[i]

        
        return ans