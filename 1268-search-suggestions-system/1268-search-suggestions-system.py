class Trie:
    def __init__(self):
        self.d = {}
    def insert(self, word):
        
        c = self.d
        for w in word:
            if w not in c:
                c[w] = {}
            c = c[w]
        c['-'] = True
        
    def search(self, prefix):
        c = self.d
        for p in prefix:
            if p not in c:
                return []
            
            c = c[p]
        
        outs = []
        def helper(d, pref):
            if '-' in d:
                outs.append(pref)
            
            l = list(d.keys())
            l.sort()
            
            for i in l:
                if i=='-':
                    continue
                pref+=i
                helper(d[i], pref)
                pref = pref[:-1]      
        
        helper(c, prefix)
        
        if len(outs)>3:
            outs = outs[:3]
        return outs

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        ans = []
        q = ""
        for s in searchWord:
            q +=s
            ans.append(trie.search(q))
        
        return ans
            