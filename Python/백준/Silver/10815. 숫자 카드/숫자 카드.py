import sys

N = int(sys.stdin.readline().rstrip()) #예제입력 5 받음
get_card = set(map(int, sys.stdin.readline().rstrip().split())) #중복을 허용하지 않는 set을 사용하여 구현. 상근이가 가지고 있는 카드 

M = int(sys.stdin.readline().rstrip()) #예제입력 8 받음 
compare_card = list(map(int, sys.stdin.readline().rstrip().split())) #비교해야 하는 카드

for i in compare_card:
	if i in get_card:
		print(1, end=" ")
	else:
		print(0, end=" ")