from collections import deque

def solution(N, k):
    
    # 1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1,N+1))

    while len(queue)>1: # deque에 하나의 요소가 남을 때까지
        for _ in range(k-1):
            queue.append(queue.popleft()) # k번째 요소를 찾기 위해 앞에서부터 제거하고 뒤에 추가
            queue.popleft() # K번째 요소 제거
    return queue[0] # 마지막으로 남은 요소 반환

print(solution(5,2))

