# Merge Sort 
def merge(a,b):
    data=[]
    x,y=len(a),len(b)
    i=j=0
    while i<x and j<y:
        if a[i]<b[j]:
            data.append(a[i])
            i+=1
        else:
            data.append(b[j])
            j+=1
    while i<x:
        data.append(a[i])
        i+=1
    while j<y:
        data.append(b[j])
        j+=1
    return data

def sort(a):
    n=len(a)
    if n==1:
        return a 
    else:
        return merge(sort(a[:n//2]),sort(a[n//2:]))
 


a = list(map(int,input().split()))
data = sort(a)
print(data)






    
