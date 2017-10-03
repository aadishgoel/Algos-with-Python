x1, y1, x2, y2 = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(x1)]
b = [list(map(int,input().split())) for _ in range(x2)]

def multiply (a,b):
    x=len(a)
    y=len(a[0])
    z=len(b)
    data = [ [0]*y for _ in range(x)]
    for i in range(x):
        for j in range(z):
            for k in range(y):
                data[i][j] += a[i][k] * b[k][j] 
    return data

data = multiply(a,b)
for row in data:
    print(*row)
