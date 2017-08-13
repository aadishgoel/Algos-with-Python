# Selection Sort
def sort(a):
    n = len(a)
    for i in range(n-1):
        m = i
        for j in range(i,n):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]
    return a


data = list(map(int,input().split()))
data = sort(data)
print(data)
