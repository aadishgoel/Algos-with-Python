x1, y1, x2, y2 = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(x1)]
b = [list(map(int,input().split())) for _ in range(x2)]

def multiply (a,b):
    #x=len(a)
    #y=len(a[0])
    #z=len(b)
    data = [[0, 0], [0, 0]]
    p= (a[0][0]+a[1][1])*(b[0][0]+b[1][1])
    q= (a[1][0]+a[1][1])*b[0][0]
    r= a[0][0]*(b[0][1]-b[1][1])
    s= a[1][1]*(b[1][0]-b[0][0])
    t= (a[0][0]+a[0][1])*b[1][1]
    u= (a[1][0]-a[0][0])*(b[0][0]+b[0][1])
    v= (a[0][1]-a[1][1])*(b[1][0]+b[1][1])
    data[0][0]= p+s-t+v
    data[0][1]= r+t
    data[1][0]= q+s
    data[1][1]= p+r-q+u
    return data

data = multiply(a,b)
for row in data:
    print(*row)
