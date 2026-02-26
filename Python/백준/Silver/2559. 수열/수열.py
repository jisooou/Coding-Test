import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

total = [0] * (N+1)
for i in range(1, N+1):
    total[i] = total[i-1] + temp[i-1]

min_limit = -10**18
for i in range(K, N+1):
    min_limit = max(min_limit, total[i]-total[i-K])
print(min_limit)