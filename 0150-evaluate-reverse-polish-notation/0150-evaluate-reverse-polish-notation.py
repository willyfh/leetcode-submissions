class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = deque()
        
        operators = set(["+", "-", "*", "/"])
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                r = int(stack.pop())
                l = int(stack.pop())
                if t == "+":
                    a = l + r
                elif t == "-":
                    a = l - r
                elif t == "*":
                    a = l * r
                else:
                    a = int(l / r)
                
                stack.append(a)
        return stack.pop()