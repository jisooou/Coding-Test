import sys

input = sys.stdin.readline
count = 0

def lower_bound(target, A):
    left, right = 0, len(A)
    while left < right: #-10 -10 2 3 3 6 7 10 10 10 
        mid = (left + right) // 2 #10 // 2 = 5 , left 0, right 10
        if A[mid] < target: #target=10, if 5 < 10 -> 6 < 10 ...-> 9 < 10 -> 10 < 10
            left = mid + 1
        else:
            right = mid 
    return left

def upper_bound(target, A):
    left, right = 0, len(A)
    while left < right: 
        mid = (left + right) // 2
        if A[mid] <= target: #5 <= 10 ... 10 <= 10 -> 11 <= 10 
            left = mid  + 1
        else: 
            right = mid
    return left 

N = int(input()) #10
A = sorted(map(int, input().split())) #6 3 2 10 10 10 -10 -10 7 3

M = int(input()) #8
B = map(int, input().split()) #10 9 -5 2 3 4 5 -10

for target in B: 
    lower = lower_bound(target, A)
    upper = upper_bound(target, A)
    print(upper - lower, end=" ")