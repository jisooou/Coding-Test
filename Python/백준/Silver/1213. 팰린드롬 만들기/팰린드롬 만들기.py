import sys
input = sys.stdin.readline

S = input().strip()
alpha = [0] * 26

for ch in S: 
    alpha[ord(ch)-ord('A')] += 1
oddCnt = 0
center = ''
for i in range(26): 
    if alpha[i] % 2 == 1: #홀수일때
        oddCnt += 1
        center = chr(i + ord('A'))
if oddCnt > 1: 
    print("I'm Sorry Hansoo")
else: 
    left_part = []
    for i in range(26): 
        left_part.append(chr(i + ord('A')) * (alpha[i] // 2))
    left = ''.join(left_part)
    print(left + center + left[::-1])
    
    