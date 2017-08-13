# Binary Search
def search(a,n,s):
    if a[n//2]==s:
        return 'Yes'
    elif n//2<n and a[n//2]>s:
        ans = search(a[:n//2],n//2,s)
    elif n//2+1<n and a[n//2]<s:
        ans = search(a[n//2+1:],n//2,s)
    else:
       return 'No'
    return ans


data = list(map(int,input().split()))
s = int(input())
n = len(data) 
print(search(data,n,s))

