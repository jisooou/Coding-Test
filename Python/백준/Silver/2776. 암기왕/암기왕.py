import sys
input = sys.stdin.readline

T = int(input()) 
for _ in range(T):
    N = int(input()) 
    info = set(map(int, input().split()))
    M = int(input())
    com_info = list(map(int, input().split()))
    for i in com_info:
        if i in info: 
            print(1)
        else:
            print(0)