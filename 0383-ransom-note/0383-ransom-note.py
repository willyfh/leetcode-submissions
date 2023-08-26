class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_map = {}
        
        for m in magazine:
            if m not in magazine_map:
                magazine_map[m] = 0
            magazine_map[m] +=1
            
        for r in ransomNote:
            if r not in magazine_map:
                return False
            if magazine_map[r] == 0:
                return False
            magazine_map[r]-=1
            
        return True