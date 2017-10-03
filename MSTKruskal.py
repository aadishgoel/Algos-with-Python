#Kruskal

n ,m = map(int,input().split())
graph = {}
edges = []
gp = { i:i for i in range(1,n+1) }
sets = { i:[i] for i in range(1,n+1) }
for _ in range(m):
    x ,y ,w = map(int,input().split())
    edges.append((x,y,w))



edges.sort(key=lambda x:x[2])
nedges=[]

for edge in edges:
    u,v,w = edge
    if gp[u]!= gp[v]:
        temp=gp[v]
        for i in sets[gp[v]]:
            gp[i]=gp[u]
            sets[gp[u]].append(i)
        del sets[temp]
        nedges.append((u,v,w))
        
print(nedges)
