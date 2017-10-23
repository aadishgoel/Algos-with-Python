# Task Scheduling with profit and deadline : Greedy

 
def scheduler(data,n):
    m=max(data,key=lambda x:x[1])
    ans = [0]*m
    data.sort(key=lambda x:x[2], reverse=True)
    
    
    






#driver
if __name__ =='__main__':
    
    n=int(input())
    data=[ tuple(map(int,input().split())) for _ in range(n)]
    ans=scheduler(data,n)
    print(ans)
