############  O(1)-O(n) Map-List ##################
class UnionFind1:
    def __init__(self, n):
        self.gp = { i:i for i in range(n)}
        self.sets = { i:[i] for i in range(n) }
    
    def union(self,i,j):
        if self.gp[i] != self.gp[j]:
            temp = self.gp[j]
            for node in self.sets[ self.gp[j] ]:
                self.gp[node] = self.gp[i]
                self.sets[self.gp[i]] += [node]
            del self.sets[temp]

    def find(self,i):
        return self.gp[i]
    

############  O(logn)-O(logn) Tree ##################

class UnionFind2:
    def __init__(self,n) -> None:
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        if self.parent[i] != i:
            return self.find(self.parent[i])
        return i
     
    def union(self, i,j): 
        self.parent[ self.find(j) ] =  self.find(i)
    
        
############  O(1)-O(1) Tree-Rank-PathCompression ##################

class UnionFind3:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        if self.parent[i]!=i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i,j):
        u,v = self.find(i), self.find(j)
        if   self.rank[u]<self.rank[v]: self.parent[u]=v
        elif self.rank[v]<self.rank[u]: self.parent[v]=u
        else:
            self.parent[v]=u
            self.rank[u]+=1
    


uf = UnionFind3(5)
uf.union(1,2)
uf.union(3,4)
print(uf.parent)