class Solution:
    def calculate(self, s: str) -> int:
        d = deque()
        
        
        arr = []
        
        temp = ""
        for c in s:
            if c == " ":
                continue
            elif c == "+" or c == "/" or c == "*" or c == "-":
                arr.append(temp)
                temp = ""
                arr.append(c)
            else:
                temp+=c
                
        arr.append(temp)
        i = 0
        while i < (len(arr)):
            c = arr[i]
            if c == "*" or c == "/":
                l = d.pop()
                i+=1
                if c == "*":
                    d.append(str(int(l)  * int(arr[i])))
                else:
                    d.append(str(int(int(l)  / int(arr[i]))))
            else:
                d.append(c)
            i+=1
        print(d)
        while len(d)>1:
            r = d.popleft()
            o = d.popleft()
            l = d.popleft()
            if o =="+":
                d.appendleft(str(int(r) + int(l)))
            else:
                d.appendleft(str(int(r) - int(l)))
                
        return int(d[0])