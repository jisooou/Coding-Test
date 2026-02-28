import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = []
pokemon_dict = {}

for i in range(1, N+1):
    name = input().strip()
    pokemon.append(name)
    pokemon_dict[name] = i
for i in range(M):
    question = input().strip()
    if question.isdigit():
        print(pokemon[int(question)-1])
    elif question.isalpha():
        print(pokemon_dict[question])