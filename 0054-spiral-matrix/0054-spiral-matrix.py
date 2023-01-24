class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        i=0
        j=0
        m = len(matrix)
        n = len(matrix[0])
        
        ans = []
        step = 0
        c = 0
        if m*n==1:
            return [matrix[0][0]]
        while c<m*n:
            while j<n-1-step and  c<m*n:
                ans.append(matrix[i][j])
                j+=1
                c+=1

            while i < m-1-step and c<m*n:
                ans.append(matrix[i][j])
                i+=1
                c+=1

            while j>0+step and c<m*n:
                ans.append(matrix[i][j])
                j-=1
                c+=1

            while i>0+step and c<m*n:
                ans.append(matrix[i][j])
                i-=1
                c+=1
            i+=1
            j+=1
            
            if c==m*n-1:
                ans.append(matrix[i][j])
                c+=1
            step+=1
                
        return ans
                