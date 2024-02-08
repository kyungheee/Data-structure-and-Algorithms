'''
핵심 : 닫힌 괄호를 처음 보는 순간 가장 마지막에 찾았던 같은 모양의 열린 괄호를 찾을 수 있어야 한다!
'''


def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):

            # 괄호 문자열을 회전시키면서 참조
            c = s[(i+j)%n] # 모듈러 연산?
            if c == "(" or c == "[" or c == "{" : # 열린 괄호를 푸시
                    stack.append(c)
            else:
                if not stack: # 짝이 맞지 않은 경우
                    break      
                
                # 닫힌 괄호는 스택의 top과 짝이 맞는지 비교
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break

        else: # for문이 break에 끝나지 않고 끝까지 수행된 경우
            if not stack:
                answer +=1
    return answer