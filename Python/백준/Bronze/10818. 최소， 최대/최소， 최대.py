import sys

N = int(sys.stdin.readline().rstrip()) #N을 정의
num = list(map(int, sys.stdin.readline().split())) #입력값을 리스트로 받음

print(min(num), max(num))