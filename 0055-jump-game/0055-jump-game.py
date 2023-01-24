class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return True

        q = deque()
        q.append(0)
        
        visited = [False]*len(nums)
        
        while len(q) >0:
            c = q.popleft()

            if c+nums[c]>=len(nums)-1:
                return True
            for i in range(c+1, c+nums[c]+1):
                if i < len(nums) and not visited[i]:
                    q.append(i)
                    visited[i] = True                    
        return False