import sys

result = 0 

N, M = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = num[i] + num[j] + num[k]
            if(sum > result and sum <= M):
                result = sum
print(result)