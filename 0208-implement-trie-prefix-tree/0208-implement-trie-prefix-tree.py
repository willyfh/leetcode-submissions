class TrieNode:
    def __init__(self, childs={}):
        self.childs = childs

class Trie:
    
    def __init__(self):
        self.trie = TrieNode({})

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w in t.childs:
                t = t.childs[w]
            else:
                t.childs[w] = TrieNode({})
                t = t.childs[w]
        t.childs['end'] = True

    def search(self, word: str) -> bool:
        t = self.trie
        for w in word:
            if w not in t.childs:
                return False
            t = t.childs[w]
        if 'end' in t.childs:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for w in prefix:
            if w not in t.childs:
                return False
            t = t.childs[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)