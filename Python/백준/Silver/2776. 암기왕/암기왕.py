import sys
input = sys.stdin.readline

T = int(input()) 
for _ in range(T):
    N = int(input())
    answer = set(map(int, input().split()))
    M = int(input())
    test = list(map(int, input().split()))
    for i in test: 
        if i in answer: 
            print(1)
        else:
            print(0)