def to_sec(t):
    m, s = map(int, t.split(':'))
    return m * 60 + s

def to_time(s):
    return f"{s//60:02d}:{s%60:02d}"

N = int(input())

team1 = 0
team2 = 0
lead1 = 0
lead2 = 0
prev = 0

for _ in range(N):
    team, t = input().split()
    cur = to_sec(t)

    if team1 > team2:
        lead1 += cur - prev
    elif team2 > team1:
        lead2 += cur - prev

    if team == '1':
        team1 += 1
    else:
        team2 += 1

    prev = cur

end = 48 * 60

if team1 > team2:
    lead1 += end - prev
elif team2 > team1:
    lead2 += end - prev

print(to_time(lead1))
print(to_time(lead2))