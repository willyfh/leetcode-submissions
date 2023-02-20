class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        b = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i]==9:
                digits[i] = 0
            else:
                digits[i]+=1
                b = True
                break
                
        if not b:
            return [1] + digits
        return digits