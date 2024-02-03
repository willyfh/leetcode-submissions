class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set({'a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O'})
        i = 0
        j = len(s)-1
        
        arr = list(s)
        while i < j:
            
            while i< len(s) and arr[i] not in vowels:
                i+=1
                
            while j>=0 and arr[j] not in vowels:
                j-=1
            
            if i > j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
                        
        return "".join(arr)