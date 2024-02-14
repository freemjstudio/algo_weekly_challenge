import heapq

def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_values = 0
    previous = 0
    length = len(food_times)
    
    while sum_values + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_values += (now - previous) * length
        length -= 1
        previous = now
    
    foods = sorted(q, key = lambda x : x[1])
    return foods[(k - sum_values) % length][1]