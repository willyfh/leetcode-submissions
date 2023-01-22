class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans_list = []
        def helper(ans, num_open, num_close):
            if len(ans)==n*2:
                ans_list.append(ans)
                return   
            if num_open < n:
                helper(ans+"(", num_open+1, num_close)
            if num_open>num_close:
                helper(ans+")", num_open, num_close+1)
                
            
        helper("", 0, 0)
        return ans_list