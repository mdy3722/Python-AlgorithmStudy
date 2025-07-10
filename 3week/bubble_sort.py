input = [4, 6, 2, 9, 1]
"""
4, 6, 2, 9, 1
-> -> -> ->
1회
i = 0
비교 4번 
4 2 6 1 9
2회 i = 1
비교 3번
2 4 1 6 9
3회
비교 2번
2 1 4 6 9
4회
비교 1번
1 2 4 6 9
"""
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j + 1], array[j]
                
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))