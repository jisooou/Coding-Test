def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        new_array = array[commands[c][0]-1:commands[c][1]]
        new_array.sort()
        answer.append(new_array[commands[c][2]-1])
    return answer