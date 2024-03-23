class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        ans = 1
        end = points[0][1]
        for p in points:
            if p[0] <= end:
                end = min(end, p[1])
            else:
                end = p[1]
                ans+=1
                
        return ans