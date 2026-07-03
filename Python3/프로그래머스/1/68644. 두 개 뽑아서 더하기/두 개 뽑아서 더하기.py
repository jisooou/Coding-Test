from itertools import combinations
def solution(numbers):
    answer = set()
    for x, y in combinations(numbers, 2):
        total = 0
        total = x + y
        answer.add(total)
    return sorted(answer)