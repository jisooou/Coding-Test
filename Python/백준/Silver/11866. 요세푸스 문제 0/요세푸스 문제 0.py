import sys
input = sys.stdin.readline

M, N = map(int, input().split()) # M:7 N:3 
data = list(range(1, M+1))
result = []
idx = 0

while data: 
    idx = (idx + (N-1)) % len(data)
    result.append(data.pop(idx))
print("<" + ", ".join(map(str, result)) + ">")