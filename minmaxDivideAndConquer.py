import random
n=8

data = [ random.randint(1,100) for _ in range(n)]
#data = [61, 63, 26, 68, 83, 13, 43, 45]
print(data)

def minmax(data,s,e):
    l=e-s
    m=(s+e)//2
    if l>2:
        return( min(minmax(data,s,m)[0],minmax(data,m,e)[0]),
                max(minmax(data,s,m)[1],minmax(data,m,e)[1]) )
    else:
        if not data[s:e]: return (10**9,-10**9)
        return min(data[s:e]) , max(data[s:e])










ans = minmax(data,0,n)
print(ans)
print(min(data),max(data))
