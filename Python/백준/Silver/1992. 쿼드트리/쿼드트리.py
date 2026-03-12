N = int(input())
dist = [list(map(int, input().strip())) for _ in range(N)]
def q_tree(x, y, size):
    first = dist[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if dist[i][j] != first:
                half = size // 2
                return (
                    "("
                    +q_tree(x, y, half)
                    +q_tree(x, y+half, half)
                    +q_tree(x+half, y, half )
                    +q_tree(x+half, y+half, half)
                    +")"
                )
    return str(first)
print(q_tree(0, 0, N))    