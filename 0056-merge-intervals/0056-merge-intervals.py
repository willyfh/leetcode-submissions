class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
        ans = []
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] <= end:
                end = max(sorted_intervals[i][1], end)
            else:
                ans.append([start, end])
                start = sorted_intervals[i][0]
                end = sorted_intervals[i][1]
                
        ans.append([start, end])
                
        return ans
            