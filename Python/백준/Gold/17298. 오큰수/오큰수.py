import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = [-1] * n
num = list(map(int, input().split()))

for i in range(n): 
    while stack and num[stack[-1]] < num[i]:
            idx = stack.pop()
            answer[idx] = num[i]
    stack.append(i)
print(*answer)