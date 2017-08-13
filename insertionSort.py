# Insertion Sort
data = list(map(int,input().split()))

def sort(data):
    n = len(data)
    i=1
    while i<n:
        temp=data[i]
        j=i
        while j>0 and data[j]>=temp:
            data[j]=data[j-1]
            j-=1
        data[j+1]=temp
        i+=1
    return data

data=sort(data)
print(data)
