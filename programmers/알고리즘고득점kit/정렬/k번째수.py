# 나의 풀이
def solution(array, commands):
    answer = []
    dict = {idx: c for idx, c in enumerate(commands)}
    n = len(dict)
    
    for i in range(n):
        start = dict[i][0] - 1
        end = dict[i][1]
        location = dict[i][2] - 1
        
        sorted_array = sorted(array[start:end])
        answer.append(sorted_array[location])
        
    return answer

# 더 간단한 버전
def solution(array, commands):
    answer = []
    # for command in commands: i,j,k = command로도 가능. 몰랐음.... 
    for i, j, k in commands:    # 참고로 문제에서 commands는 [[2,2,1], [4,5,2], [8,5,4]] 같은 2차원배열 - i,j,k = 2,2,1 이렇게 빼낼 수 있음!!!!
        sliced = sorted(array[i-1:j])  # i-1부터 j까지 슬라이싱 후 정렬
        answer.append(sliced[k-1])     # k번째 수 추가
    return answer
