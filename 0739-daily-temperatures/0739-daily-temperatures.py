class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        d = deque()
        d.append(0)

        for i in range(1, len(temperatures)):
            while d and temperatures[i] > temperatures[d[-1]]:
                j = d.pop()
                ans[j] = i-j
            d.append(i)
            
        return ans