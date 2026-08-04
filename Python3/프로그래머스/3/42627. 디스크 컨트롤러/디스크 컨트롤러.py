import heapq
def solution(jobs):
    jobs.sort()
    heap = []
    current_time = 0
    current_idx = 0
    complete = 0
    answer = 0
    while complete < len(jobs):
        while current_idx < len(jobs) and jobs[current_idx][0] <= current_time:
            start_time, duration = jobs[current_idx]
            heapq.heappush(heap, (duration, start_time))
            current_idx += 1
            
        if heap:
            duration, start_time = heapq.heappop(heap)
            current_time += duration
            answer += current_time - start_time
            complete += 1
        else:
            current_time = jobs[current_idx][0]
    return answer // len(jobs)