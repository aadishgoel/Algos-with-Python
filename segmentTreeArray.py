# Segment Tree Array
from math import log2, ceil

#Defaults
def f(*args, **kwargs):
    return max(*args, **kwargs)
default = 0 


def create_tree(temp):
    #Initialising
    n = len(temp)
    m = 2**(ceil(log2(n)))
    data = [(n,m,n+m)] + [(-1,-1,default)]*(m-1)
    for i,value in enumerate(temp):
        data.append((i,i,value))

    #Framing Tree
    i=data[0][2]-1
    if i%2==0:
        data[i//2]=data[i]
        i-=1
    while i>1:
        data[i//2]=( data[i-1][0], data[i][1], f(data[i-1][2],data[i][2]) )
        i-=2
    return data
    
def update(data, pos, value): 
    i = data[0][1]+pos
    data[i] = (data[i][0], data[i][1] ,value)
    if i%2==0:
        if i+1<data[0][2]:
            data[i//2]=( data[i][0], data[i+1][1], f(data[i][2],data[i+1][2]) )
        else:
            data[i//2]=data[i]
        i-=1
    while i>1:
        data[i//2]=( data[i-1][0], data[i][1], f(data[i-1][2],data[i][2]) )
        i-=2

def query(data,x,y):
    def recurse(data,i,x,y):
        #print(i)
        if x == data[i][0] and y == data[i][1]:
            ans=data[i][2]
        elif y <= data[i][1]:
            ans=recurse(data,i*2,x,y)
        elif x > data[i][1]:
            ans=recurse(data,i+1,x,y)
        else:
            ans = f( recurse(data,i,x,data[i][1]), recurse(data,i+1,data[i+1][0],y) )
        return ans
    return recurse(data,1,x,y)    
    
  
#Driver
raw = list(map(int, input().split()))
tree = create_tree(raw)


