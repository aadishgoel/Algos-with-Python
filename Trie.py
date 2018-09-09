# Trie :AAG

class TrieNode:
    def __init__(self):
        self.nodes = [None]*2
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def converter(self, s): return int(s)

    def search(self, keys):
        p = self.root
        flag=0
        for i in range(len(keys)):
            key = self.converter(keys[i])
            if not p.nodes[key]: flag=1; break
            else: p = p.nodes[key]
        if flag: return []
        return p
    
    def insert(self, keys):
        p = self.root
        for i in range(len(keys)):
            key = self.converter(keys[i])
            if not p.nodes[key]: p.nodes[key] = TrieNode(); p = p.nodes[key]
            else: p = p.nodes[key]
        p.isEnd = True 
            
    def trieprint(self,t,s):
        global ans
        for i in range(2):
            if t.nodes[i]: self.trieprint(t.nodes[i],s+str(i))
        if t.isEnd: ans.append(s)

ans=[]
t = Trie()
t.insert('10101')
t.insert('101')
t.insert('10100')
t.trieprint(t.search('1010'),'')

print('ans:', ans)
    
    
