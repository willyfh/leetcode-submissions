class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        operators = set(["+", "-", "*", "/"])
        
        for i in range(len(tokens)):
            
            if tokens[i] in operators:
                right = stack.pop()
                left = stack.pop()
                
                res = None
                if tokens[i] == "+":
                    res = left + right
                elif tokens[i] == "-":
                    res = left - right
                elif tokens[i] == "*":
                    res = left * right
                else:
                    res = int(left / right)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
                
        return stack[0]