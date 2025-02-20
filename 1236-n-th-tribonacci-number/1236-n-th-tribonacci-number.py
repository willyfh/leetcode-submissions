class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n<3:
            return t[n]
        for i in range(3, n+1):
            t.append(t[i-3] + t[i-2] + t[i-1])
        return t[-1]