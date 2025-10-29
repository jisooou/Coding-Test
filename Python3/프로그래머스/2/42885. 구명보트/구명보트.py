# 그리디 문제
# 구명보트를 최대한 적게 사용해서 모든 사람 구출한다. 
# 조건만 생각한다 -> 어떤 것만 알면 되나? 
# 1. 가벼운 사람 + 무거운 사람 
# 2. 무거운 사람만 
def solution(people, limit):
    boat = 0
    people.sort()
    left, right = 0, len(people)-1
    while (left <= right):
        if people[left] + people[right] <= limit: 
            left += 1 
        right -= 1
        boat += 1
    return boat