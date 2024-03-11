class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        fr = {}
        to = {}
        for eq, val in zip(equations, values):
            if eq[0] not in fr:
                fr[eq[0]] =[]
            fr[eq[0]].append((eq[1], val))
            
            if eq[1] not in to:
                to[eq[1]] =[]
                
            to[eq[1]].append((eq[0], 1/val))
            
        
        self.ans = []
    
        for i,q in enumerate(queries):
            self.visited = {}
            if q[0] not in fr and q[0] not in to or q[1] not in fr and q[1] not in to:
                self.ans.append(-1)
                continue
            if q[0] == q[1]:
                self.ans.append(1)
                continue
            self.helper(q[0], q[1], fr, to, 1)
            if len(self.ans) == i:
                self.ans.append(-1)
            
        return self.ans
            
                
    def helper(self, start, end, fr, to, ans):
        
        if (start, end) in self.visited:
            return
        self.visited[(start, end)] = 1
        
        if start in fr:
            for f in fr[start]:
                if (f[0], end) in self.visited:
                    continue
                ans *= f[1]
                if f[0] == end:
                    self.ans.append(ans)
                self.helper(f[0], end, fr, to, ans)
                ans /= f[1]
        if start in to:
            for t in to[start]:
                if (t[0], end) in self.visited:
                    continue
                ans *= t[1]
                if t[0] == end:
                    self.ans.append(ans)
                self.helper(t[0], end, fr, to, ans)
                ans /= t[1]
                