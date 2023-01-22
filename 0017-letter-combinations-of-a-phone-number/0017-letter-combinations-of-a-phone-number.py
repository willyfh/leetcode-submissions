class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {}
        m[2] = "abc"
        m[3] = "def"
        m[4] = "ghi"
        m[5] = "jkl"
        m[6] = "mno"
        m[7] = "pqrs"
        m[8] = "tuv"
        m[9] = "wxyz"
        
        ans_list = []
        def helper(ans, i):
            if len(ans)==len(digits):
                ans_list.append(ans)
                return
            for a in m[int(digits[i])]:
                helper(ans+a, i+1)
                
        if len(digits)==0:
            return []
        helper("", 0)
        return ans_list

            
        