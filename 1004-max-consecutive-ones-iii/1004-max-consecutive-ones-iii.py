class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        q = deque()
        
        ans_temp = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==1:
                ans_temp+=1
            else: # 0
                if len(q) < k:
                    q.append(i)
                    ans_temp+=1
                else:
                    if len(q) > 0:
                        idx = q.popleft()
                        q.append(i)
                        ans_temp = i - idx
                    else:
                        ans_temp = 0
            ans = max(ans, ans_temp)
            
        return ans