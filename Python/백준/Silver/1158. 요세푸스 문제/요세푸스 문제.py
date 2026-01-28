import sys 
input = sys.stdin.readline

M, N = map(int, input().split()) # 7 3

idx = 0 
data = list(range(1, M+1))
result = []

while data: 
    idx = (idx + (N-1)) % len(data)
    result.append(data.pop(idx))
print("<" + ", ".join(map(str, result)) + ">")