import sys 
input = sys.stdin.readline

N = input().strip()

cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in cro_list: 
    N = N.replace(i, "*")
print(len(N))