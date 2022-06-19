import sys
from sys import stdin
def mcm(p,i,j, dp):
    if i == j:
        return 0
    min_value = sys.maxsize
    for k in range(i,j):
        if(dp[i][k] == -1):
            ans1 = mcm(p, i, k, dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
        if(dp[k+1][j] == -1):
            ans2 = mcm(p, k+1, j, dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]
        
        mCost = p[i-1]*p[k]*p[j]
        current_value = ans1 +ans2+mCost
        min_value = min(min_value, current_value)
    return min_value
    	
    

n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
dp = [[-1 for j in range(n+1)] for i in range(n+1)]
print(mcm(p,1,n, dp))