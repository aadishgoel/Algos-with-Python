#  Linear Search
def search(data,s):
    for i,item in enumerate(data):
        if item==s:
            return i
            break
    else:
        return None


data = list(map(int,input().split()))
s = int(input())
ans = search(data,s)
print('Yes' if ans else 'No')
