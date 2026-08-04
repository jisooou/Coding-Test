import heapq
def solution(jobs):
    jobs.sort()
    heap = []
    complete = 0
    job_idx = 0
    current_time = 0
    total = 0
    while complete < len(jobs):
        while job_idx < len(jobs) and jobs[job_idx][0] <= current_time:
            start, duration = jobs[job_idx]
            heapq.heappush(heap, (duration ,start))
            job_idx += 1
        if heap:
            duration, start = heapq.heappop(heap)
            current_time += duration
            total += current_time - start
            complete += 1
        else:
            current_time = jobs[job_idx][0]
    return total // len(jobs)