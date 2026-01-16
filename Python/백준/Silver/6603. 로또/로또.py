import sys 
input = sys.stdin.readline

def dfs(start):
    if(len(path) == 6):
        print(*path)
        return
    for i in range(start, N):
        path.append(M[i])
        dfs(i+1)
        path.pop()
    
while True: 
    data = list(map(int, input().split()))
    if(data[0] == 0):
        break
    N = data[0] # 7 
    M = data[1:] # 나머지 값들 
    path = []
    
    dfs(0)
    print()