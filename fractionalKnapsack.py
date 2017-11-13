# Fractional Knapsack

wt = [40,50,30,10,10,40,30]
pro = [30,20,20,25,5,35,15]
n = len(wt)
data = [ (i,pro[i],wt[i]) for i in range(n) ]

bag = 100
data.sort(key=lambda x: x[1]/x[2], reverse=True)

profit=0
ans=[]

i=0
while i<n:
    if data[i][2]<=bag:
        bag-=data[i][2]
        ans.append(data[i][0])
        profit+=data[i][1]
        i+=1
    else:
        break

if i<n:
    ans.append(data[i][0])
    profit += (bag*data[i][1])/data[i][2]
    
print(profit,ans)
