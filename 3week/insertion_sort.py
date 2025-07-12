input = [4, 6, 2, 9, 1]

'''
    1 
    1  2 
[4, 6, 2, 9, 1]
4 6 비교 -> 4는 이미 정렬,, 즉 인덱스 1부터 시작 => 1, 0 비교
6, 2 비교 -> 인덱스 2부터,, 그 다음 4, 2, 6에서 4와 2 비교 -> 인덱스 2, 1, 0
...
총 4회

최선(오메가)일때는 N만큼만,,
1부터 5
j는 i=1에서 1번, i=2에서 2번 비교,,, => for j in range(i)
i = 1, j = 0 => i - j = 1
i = 2, j = 0 1 -> i - j = 2, 1
'''

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break
            
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))