import sys
from itertools import combinations
input = sys.stdin.readline

x = [int(input()) for _ in range(9)]
x.sort()

for comb in combinations(x, 7):
    if sum(comb) == 100:
        for i in comb:
            print(i)
        break