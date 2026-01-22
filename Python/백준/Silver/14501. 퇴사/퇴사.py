import sys
input = sys.stdin.readline

line = int(input())

N = [0] * line
M = [0] * line

for i in range(line):
    N[i], M[i] = map(int, input().split())
    
dp = [0] * (line+1)

for i in range(line-1, -1, -1):
    if i + N[i] <= line: 
        dp[i] = max(dp[i+1], M[i] + dp[i + N[i]])
    else: 
        dp[i] = dp[i+1]
        
print(dp[0])