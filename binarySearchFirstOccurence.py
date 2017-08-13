#  Binary Search First Occurence
def search(data,s):
    n=len(data)
    i,j=0,n-1
    while True:
        mid=(i+j)//2
        if (mid==0 or data[mid-1]<s) and data[mid]>=s:
            return mid
        elif data[mid]<s:
            i=mid+1
        elif data[mid]>=s:
            j=mid-1
        else:
            return None
    

data = list(map(int,input().split()))
s = int(input())
#print('********************')
ans=search(data,s)
print(ans)
