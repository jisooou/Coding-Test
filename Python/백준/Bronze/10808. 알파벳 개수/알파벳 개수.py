import sys 
input = sys.stdin.readline

S = input().strip()
cnt = [0] * 26 

for ch in S: 
    cnt[ord(ch)-ord('a')] += 1
print(*cnt)