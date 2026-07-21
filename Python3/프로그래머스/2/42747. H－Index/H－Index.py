def solution(citations):
    citations.sort() 
    for i in range(len(citations)):
        remain = len(citations) - i
        if remain <= citations[i]:
            return remain
    return 0