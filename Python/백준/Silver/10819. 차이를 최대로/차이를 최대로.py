import sys
from itertools import permutations 

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))

answer = 0 

for perm in permutations(M): 
    total = 0 
    for i in range(N-1):
        total += abs(perm[i] - perm[i+1])
    answer = max(total, answer)
print(answer)