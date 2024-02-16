class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        ans = 0
        s = 0
        for g in gain:
            s += g
            ans = max(ans, s)
        return ans