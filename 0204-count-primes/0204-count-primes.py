import numpy
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
        arr = [True]*n
        arr[0] = False
        arr[1] = False
        

        ans =0 
        for i in range(2, n):
            if not arr[i]:
                continue
            
            ans += 1
            arr[i] = True
            # j = i*i
            # while j < n:
            #     arr[j] = False
            #     j += i
            for j in range(i*i, n, i):
                arr[j] = False

        return ans

    
