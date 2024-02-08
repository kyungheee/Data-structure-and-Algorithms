'''
1. 현지 주식보다 이전 주식의 가격이 높으면 이전 주식의 길이를 확정한다.
2. 이전 주식들을 하나씩 보고 현재 주식 가격보다 큰 주식 가격이 있다면 그 주식의 길이를 확정한다.
3. 길이를 확정한 주식은 이후 계산에서 제외한다.

- 결국 스택에 남는 원소는 길이를 확정하지 않은, 다시 말해 가격이 끝까지 떨어지지 않은 주식
- 스택에 푸시하는 값은 주식의 가격이 아니라 인덱스
'''

def solution(prices):
    n = len(prices)
    answer = [0]*n # 가격이 떨어지지 않은 기간을 저장할 배열

    # 스택을 사용해 이전 가격과 현재 가격 비교
    stack = [0] # 스택 초기화
    for i in range(1,n):
        while stack and prices[i] <prices[stack[-1]]:
            # 가격이 떨어졌으므로 이전 가격의 기간 계산
            j = stack.pop()
            answer[j] = i-j
        stack.append()
    # 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n-1-j
    
    return answer