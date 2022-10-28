class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = deque()
        for n in nums:
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
                            ans.popleft()
                            temp = ans.pop()
                            ans.append(n)
                            ans.append(temp)
                        else:
                            ans.popleft()
                            ans.appendleft(n)
                    elif len(ans)==2:
                        temp = ans.pop()
                        ans.append(n)
                        ans.append(temp)
        return ans[0] if len(ans)==3 else ans[-1]
            
            