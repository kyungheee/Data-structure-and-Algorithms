def solution(decimal):
    num = decimal
    n = []
    while num != 0:
        r = num % 2
        n.append(str(r))
        num = num // 2
    n.reverse()
    return int(''.join(n))

print(solution(10))
print(solution(27))
print(solution(12345))
