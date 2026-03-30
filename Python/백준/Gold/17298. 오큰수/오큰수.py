import sys
input = sys.stdin.readline 

n = int(input())
num = list(map(int, input().split()))

stack = []
answer = [-1] * n

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        idx = stack.pop()
        answer[idx] = num[i]
    stack.append(i)
print(*answer)