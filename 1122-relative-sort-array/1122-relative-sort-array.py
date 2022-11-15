class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        notExist = []       
        countMap = {}
        
        set2 = set()
        
        for a in arr2:
            set2.add(a)
        
        for a in arr1:
            if a not in countMap:
                countMap[a] = 0
            countMap[a] += 1
            if a not in set2:
                notExist.append(a)
        
        out = []
        for a in arr2:
            while countMap[a]>0:
                out.append(a)
                countMap[a]-=1
        
        notExist.sort()
        for n in notExist:
            out.append(n)
        
        return out