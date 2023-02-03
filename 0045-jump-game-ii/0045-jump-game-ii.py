class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        q = deque()
        
        q.append((0,0))
        
        visited = [0]*len(nums)
        while len(q) > 0:
            i, lvl = q.popleft()
            
            for j in range(i+1, i+nums[i]+1):
                if j == len(nums)-1:
                    return lvl + 1
                if visited[j] == 0:
                    q.append((j, lvl+1))
                    visited[j] = 1