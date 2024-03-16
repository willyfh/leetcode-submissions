class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        ans = []
        
        potions.sort()
        
        for s in spells:
            ans.append(self.count(s, potions, success))
        
        return ans
            
            
    def count(self, s, potions, target):
        
        left = 0
        right = len(potions)-1
        
        while left <= right:
            
            mid = (left + right)//2
            
            if (mid == 0 or potions[mid-1]*s < target) and potions[mid] * s >= target:
                return len(potions) - mid
            elif potions[mid] * s >= target:
                
                right = mid-1
            else:
                left = mid+1
        return 0
            
            
            
        
        