import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word_list = {}

for _ in range(n):
    word = input().strip()
    if len(word) < m: 
        continue
    else: 
        if word in word_list: 
            word_list[word] += 1
        else: 
            word_list[word] = 1
result = sorted(word_list.keys(), key = lambda x : (-word_list[x], -len(x), x))

for r in result: 
    print(r)