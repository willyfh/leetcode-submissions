class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        ans = 1
        start = points[0][0]
        end = points[0][1]
        for p in points:
            if p[0] <= end:
                start = p[0]
                end = min(end, p[1])
            else:
                start = p[0]
                end = p[1]
                ans+=1
                
        return ans