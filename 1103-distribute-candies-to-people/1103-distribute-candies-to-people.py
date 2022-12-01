class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        i=0
        ans = [0] * num_people
        j = 1
        while candies > 0:
            if i==num_people:
                i=0
            
            if candies>= j:
                ans[i] += j
            else:
                ans[i] += candies
                
            candies -= j
            j+=1
            i+=1
            
        return ans