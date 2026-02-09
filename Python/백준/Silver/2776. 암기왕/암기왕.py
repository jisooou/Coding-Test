import sys
input = sys.stdin.readline

T = int(input()) 
for _ in range(T):
    _ = int(input()) # N
    answer = set(map(int, input().split()))
    _ = int(input()) # M
    test = list(map(int, input().split()))
    for i in test: 
        if i in answer: 
            print(1)
        else:
            print(0)