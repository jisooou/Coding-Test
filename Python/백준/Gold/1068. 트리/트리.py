import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
erase_node = int(input())

tree = [[] for _ in range(n)]
root = 0

for i in range(n):
    if parent[i] == -1: 
        root = i 
    else: 
        tree[parent[i]].append(i)
        
def dfs(node):
    child_cnt = 0
    leaf_cnt = 0 
    
    for child in tree[node]:
        if child == erase_node: 
            continue
        child_cnt += 1
        leaf_cnt += dfs(child)
        
    if child_cnt == 0: 
        return 1
    return leaf_cnt 

if erase_node == root:
    print(0)
else: 
    print(dfs(root))