
# 입력값 n에 대하여 약 n만큼의 시간 복잡도
# 운 좋으면 1만큼의 연산으로 수행이 종료 될 수 있음 -> 빅 오메가
# 운이 좋지 않다면 n만큼 걸림 -> 최악의 경우(빅오)
def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for element in array:
        if number == element:
            return True
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))