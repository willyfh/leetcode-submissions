class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans  = 0
        m = 1
        for i in range(len(columnTitle)-1, -1, -1):
            ans += m*(ord(columnTitle[i]) - ord("A")  + 1)
            m *= 26
        return ans
            