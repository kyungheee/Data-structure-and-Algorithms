'''
가장 최근에 탐색한 데이터를 먼저 비교한다 => 스택의 구조
짝이 맞는 문자를 제거한 다음 문자열을 붙이는 연산은 팝 연산으로 자연스럽게 해결할 수  있으므로 구현 시 고려할 필요 없음
'''


def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c: # 스택이 비어 있지 않고, 현재 문자와 스택의 맨 위 문자가 같으면
            stack.pop() # 스택의 맨 위 문자 제거
        else:
            stack.append(c) # 스택에 현재 문자 추가
    return int(not stack) # 스택이 비어 있으면 1, 그렇지 않으면 0 반환