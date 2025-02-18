import sys

n = int(sys.stdin.readline().rstrip())
l = dict() #딕셔너리 자료형을 사용한다. 

for _ in range(n):
    name, status = map(str, sys.stdin.readline().rstrip().split())
    if status == 'enter':
        l[name] = status
    else:
        del l[name]
        
l = sorted(l.keys(), reverse=True)

for i in l:
    print(i)