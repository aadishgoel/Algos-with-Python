#Prims

n ,m = map(int,input().split())
graph = {}
edges = []
vmark = { i:0 for i in range(1,n+1) } 
emark = { i:0 for i in range(m) }
for _ in range(m):
    x ,y ,w = map(int,input().split())
    edges.append((x,y,w))


edges.sort(key=lambda x:x[2])
nedges=[]
start=int(input())
vmark[start]=1              

for _ in range(n-1):
    for i in range(m):
        if emark[i]: continue
        u,v,w = edges[i]
        if vmark[u] != vmark[v]:
            vmark[v]=1
            vmark[u]=1
            emark[i]=1
            nedges.append(edges[i])
            break

#print(nedges)
s=0
for i in nedges:
    s+=i[2]
print(s)
