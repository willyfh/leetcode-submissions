class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # see topological sort
        
        d = [[] for i in range(numCourses)]
        nodeInDegree = [0]*numCourses
        
        
        # build the graphs and calculate incoming degree for each node
        for k,v in prerequisites:
            nodeInDegree[k] += 1
            d[v].append(k)
            
        # add nodes which have zero incoming degree to the queue
        q = deque()
        for i in range(numCourses):
            if nodeInDegree[i] == 0:
                q.append(i)
        
        ans = []
        while len(q) > 0:
            node = q.popleft()
            ans.append(node)
            
            for c in d[node]:
                nodeInDegree[c] -= 1
                if nodeInDegree[c] == 0:
                    q.append(c)
                    
        if len(ans) == numCourses:
            return ans
        return []