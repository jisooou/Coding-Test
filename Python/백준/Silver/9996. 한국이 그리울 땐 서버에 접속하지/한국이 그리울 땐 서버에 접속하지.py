import sys
input = sys.stdin.readline

N = int(input()) # 3
pre, suf = input().strip().split("*")

for _ in range(N):
    word = input().rstrip()
    if len(word) < len(pre) + len(suf):
        print("NE")
        continue
    
    if word.startswith(pre) and word.endswith(suf):
        print("DA")
    else:
        print("NE")