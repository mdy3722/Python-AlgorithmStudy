input = [4, 6, 2, 9, 1]
"""
총 정렬 횟수 : 4번
46291
16294 -> arr[0], arr[n-1]
12694 -> arr[1], target
12496 -> arr[2], target
12469 -> arr[3]
"""
# O(N^2)
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i     # i = 0
        for j in range(n - i): # j = 0..4
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]        

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))