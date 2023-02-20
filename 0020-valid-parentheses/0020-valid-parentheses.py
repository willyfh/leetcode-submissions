class Solution:
    def isValid(self, s: str) -> bool:
        op = set({"(","[","{"})
        cl = {")" : "(", "]" : "[", "}" : "{"}
        
        stack = deque()
        for i in range(len(s)):
            if s[i] in op:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                o = stack.pop()
                if cl[s[i]] != o:
                    return False
                
        return len(stack)==0