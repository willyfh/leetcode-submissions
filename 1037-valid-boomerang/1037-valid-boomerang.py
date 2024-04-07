class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        s = set()
        d = set()
        
        prev_point = None
        for point in points:
            if (point[0], point[1]) in s:
                return False
            s.add((point[0], point[1]))
            if not prev_point:
                prev_point = point
            else:
                if point[0]-prev_point[0] == 0:
                    d.add(float("inf"))
                else:
                    d.add(((point[1]-prev_point[1])/(point[0]-prev_point[0])))
                    prev_point = point
        if len(d) == 1:
            return False
        return True