'''
큐(queue)는 '줄을 서다'라는 뜻
먼저 들어간 데이터가 먼저 나오는 자료구조 (선입선출, FIFO)
'''

queue = []

# 큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

# 큐의 맨 앞 데이터 제거
first_item = queue.pop(0)
print(first_item) # 출력 : 1

# 큐에 데이터 추가
queue.append(4)
queue.append(5)

# 큐의 맨 앞 데이터 제거
first_item = queue.pop(0)
print(first_item) # 출력 : 2

'''
덱을 큐처럼 활용하기
덱 : Double Ended Queue (양 끝에서 삽입이나 삭제할 수 있는 큐)
'''

from collections import deque

queue = deque()

queue.append(3)

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(first_item) # 1

# 큐에 데이터 추가
queue.append(4)
queue.append(5)

# 큐의 맨 앞 데이터 제거 
first_item = queue.popleft()
print(first_item) # 2