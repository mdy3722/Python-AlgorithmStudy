array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index+=1
        else:
            result.append(array2[array2_index])
            array2_index+=1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index+=1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index+=1
    
    return result

# merge 연산량O(N) 곱하기 merge 함수 호출 횟수 O(logN) -> O(NlogN)
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])  # 왼쪽 부분을 정렬하고
    right_array = merge_sort(array[mid:]) # 오른쪽 부분을 정렬한 다음에
    #print(left_array, right_array)
    return merge(left_array, right_array)        # 합치면서 정렬하면 됩니다!


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))