N = int(input()) 

for i in range(N):
    total = i + sum(map(int, str(i)))
    if (total == N):
        print(i)
        break
else:
    print(0)