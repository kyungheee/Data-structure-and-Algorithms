stack = []
max_size = 10

def isFull(stack):
    # 스택이 가득 찼는지 확인하는 함수
    return len(stack) == max_size

def isEmpty(stack):
    # 스택이 비어 있는지 확인하는 함수
    return len(stack) == 0

def push(stack, item):
    # 스택에 데이터를 추가하는 함수
    if isFull(stack):
        print('스택이 가득찼습니다.')
    else:
        stack.append(item)
        print('데이터가 추가되었습니다.')

def pop(stack):
    # 스택에서 데이터를 꺼내는 함수
    if isEmpty(stack):
        print('스택이 비어 있습니다.')
        return None
    else:
        return stack.pop()
        