class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        
        vote = deque()

        n=len(senate)
        
        name_mapping = {'R': 'Radiant', 'D': 'Dire'}
        
        for s in senate:
            vote.append(s)
        i=0
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
            temp.reverse()
            for t in temp:
                vote.appendleft(t)
            
            
            
            
                