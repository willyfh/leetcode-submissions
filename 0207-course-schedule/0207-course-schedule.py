class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        
        def helper(i, s):
            if v[i]:
                s = set()
                return True
            
            if prerequisites[i][1] not in d:
                v[i] = True
                s = set()
                return True
            
            if i in s:
                return False
            s.add(i)
            for x in d[prerequisites[i][1]]:
                if not helper(x, s):
                    return False
            v[i] = True
            s = set()
            return True     
            
        
        d = {}
        
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in d:
                
                d[prerequisites[i][0]] = []
                
            d[prerequisites[i][0]].append(i)
        
        v = [False] * len(prerequisites)
        
        
        for i in range(len(prerequisites)):
            if not helper(i, set()):
                return False
            
            
        return True