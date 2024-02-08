from collections import deque

def solution(N, k):
    # 1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1,N+1))

    while len(queue)>1:
        for _ in range(K-1):
            queue.append(queue.popleft())

            