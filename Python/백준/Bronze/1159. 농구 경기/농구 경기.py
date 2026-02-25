import sys
input = sys.stdin.readline

N = int(input()) #18 
cnt = [0] * 26 

for _ in range(N):
    S = input().strip()
    cnt[ord(S[0]) - ord('a')] += 1
ans = []
for i in range(26):
    if cnt[i] >= 5:
        ans.append(chr(i + ord('a')))
if ans: 
    print(''.join(ans))
else: 
    print("PREDAJA")