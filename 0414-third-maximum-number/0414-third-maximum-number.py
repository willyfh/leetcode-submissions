class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        ans = deque()
        m = float("-inf")
        for n in nums:
            m = max(m, n)
            if len(ans)==0:
                ans.append(n)
            else:
                if n < ans[0]:
                    if len(ans)<3:
                        ans.appendleft(n)
                elif n > ans[-1]:
                    ans.append(n)
                    if len(ans) > 3:
                        ans.popleft()
                elif n>ans[0] and n < ans[-1]:
                    if len(ans)==3 and n!=ans[1]:
                        if n > ans[1]:
                            ans = deque([ans[1]]+[n]+[ans[-1]])
                        else:
                            ans = deque([n]+[ans[1]]+[ans[-1]])
                    elif len(ans)==2:
                        ans = deque([ans[0]]+[n]+[ans[-1]])
        return ans[0] if len(ans)==3 else ans[-1]
            
            