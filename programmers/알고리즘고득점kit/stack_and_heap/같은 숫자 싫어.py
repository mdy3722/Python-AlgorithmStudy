# 나의 풀이이
def solution(arr):
    answer = []
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    
    answer.append(arr[-1])

    return answer

# 다른 풀이
def no_continuous(s):
    result = []
    for c in s:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue   # a[-1:]은 a가 비어있으면 []을 반환
        a.append(i)
    return a