def solution(arr, target):
    answer='True'
    dict1= {}
    for i in range(len(arr)):
        dict1[arr[i]]=i

    for key, value in dict1.items():
        findValue= target-key
        if findValue == key:
            continue
        if findValue in dict1:
            answer='True'
            break
        else:
            answer='False'

    return answer