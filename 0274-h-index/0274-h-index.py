class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        citations.sort(reverse=True)
        
        for i, c in enumerate(citations):
            if c<=i:
                return i
            
        return i+1
            
        