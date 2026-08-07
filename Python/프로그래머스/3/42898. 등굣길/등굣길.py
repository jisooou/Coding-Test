def solution(m, n, puddles):
    dp = [[0]*m for i in range(n)]
    dp[0][0] = 1
    puddle_set = {(y-1, x-1) for x, y in puddles}
    
    for i in range(n):
        for j in range(m):
            if (i, j) in puddle_set:
                dp[i][j] = 0
                continue
                
            #아래쪽으로 이동
            if i > 0:
                dp[i][j] += dp[i-1][j] 
             #오른쪽으로 이동
            if j > 0:
                dp[i][j] += dp[i][j-1]
            
            dp[i][j] %= 1000000007
    return dp[n-1][m-1]