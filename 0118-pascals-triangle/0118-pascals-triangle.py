class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return  [[1],[1,1]]
        
        ans = [[1],[1,1]]
        for i in range(3, numRows+1):
            temp = []
            for j in range(i):
                if j == 0:
                    temp.append(1)
                elif j == i-1:
                    temp.append(1)
                    
                else:
                    temp.append(ans[i-2][j] + ans[i-2][j-1])
                    
            ans.append(temp)
        return ans