def solution(n, k, cmd):
    result = ['O'] * n
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    delete = []
    selected = k + 1
    for c in cmd : 
        if c.startswith('C') :
            delete.append(selected)
            up[down[selected]] = up[selected]
            down[up[selected]] = down[selected]
            selected = up[selected] if n < down[selected] else down[selected]
        elif c.startswith('Z') :
            z = delete.pop()
            up[down[z]] = z
            down[up[z]] = z
        else :
            a, b = c.split()
            if a == 'U':
                for _ in range(int(b)):
                    selected = up[selected]
            else :
                for _ in range(int(b)):
                    selected = down[selected]
    for i in delete:
        result[i-1] = 'X'
    return ''.join(result)
