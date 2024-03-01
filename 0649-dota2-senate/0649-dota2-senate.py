class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        vote = deque()
        
        name_mapping = {'R': 'Radiant', 'D': 'Dire'}
        
        for s in senate:
            vote.append(s)
            
        while vote:
            curr = vote.popleft()
            vote.append(curr)

            temp = []
            while vote and vote[0] == curr:
                curr = vote.popleft()
                temp.append(curr)
                
            if not vote:
                return name_mapping[curr]
            
            vote.popleft()
            for i in range (len(temp)-1, -1, -1):
                vote.appendleft(temp[i])
            
            
            
            
                