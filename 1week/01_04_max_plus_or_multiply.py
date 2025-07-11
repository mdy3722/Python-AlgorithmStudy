#나의 풀이
def find_max_plus_or_multiply1(array):
    # 이 부분을 채워보세요!
    result = array[0]
    for index in range(1, len(array)):
        if result == 0:
            result = result+array[index]
        elif result+array[index] > result*array[index]:
            result = result+array[index]
        else:
            result = result*array[index]
    return result
# 시간 복잡도 -> O(N)

# 딩코딩코님 풀이
def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    sum = 0         # 대입 연산 1
    for num in array:       # N 길이만큼 비교
        if num <= 1 or sum <= 1:    # 비교 <- 이게 하이라이트
            sum += num  # 대입
        else:
            sum *= num  # 대입
    return sum

# 시간 복잡도 -> O(N)

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))