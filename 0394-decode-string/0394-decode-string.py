class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = deque()
        
        for i in range(len(s)):
            
            char = s[i]
            if char != "]":
                stack.append(s[i])
            else:
                e = stack.pop()
                encoded_string = ""
                while e != "[":
                    encoded_string = e + encoded_string
                    e = stack.pop()
                
                num = ""
                while len(stack)>0 and stack[-1].isnumeric():
                    num = stack.pop() + num
                
                k = int(num)
                while k>0:
                    for j in range(len(encoded_string)):
                        stack.append(encoded_string[j])
                    k-=1
                    
        return "".join(stack)