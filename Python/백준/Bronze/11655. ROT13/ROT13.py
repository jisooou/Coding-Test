import sys
input = sys.stdin.readline

S = input().rstrip()
answer = []
for ch in S: 
    if 'A' <= ch <= 'Z':
         answer.append(chr((ord(ch)-ord('A')+13) % 26 + ord('A')))
    elif 'a' <= ch <= 'z': 
         answer.append(chr((ord(ch)-ord('a')+13) % 26 + ord('a')))
    else: 
        answer.append(ch)
print(''.join(answer))