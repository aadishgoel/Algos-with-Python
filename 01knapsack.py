#0 1 knapsack
wt =  [1,3,4,5]
pro = [1,4,5,7]
bag = 7
n = len(wt)
dp = [ [0]*(bag+1) for _ in range(n+1) ]

for i in range(1,n+1):
    for j in range(1,bag+1):
        if j<wt[i-1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],pro[i-1]+dp[i-1][j-wt[i-1]])  

for row in dp:
    print(*row)

profit=dp[-1][-1]
print(profit)
