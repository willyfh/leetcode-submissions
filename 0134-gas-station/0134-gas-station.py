class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        c = 0
        start = 0
        end = False
        i=0
        while i <len(gas):
            
            tank += gas[i]
            if tank>=cost[i]:
                tank -= cost[i]
                c+=1
            else:
                if end: break
                tank = 0
                c=0
                start = i+1
            
            if c == len(gas):
                return start
            
            i+=1
            if i==len(gas):
                end = True
                i=0
                
        return -1