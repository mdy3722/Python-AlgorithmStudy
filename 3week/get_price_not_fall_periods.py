prices = [1, 2, 3, 2, 3]
'''
1 2 3 2 3
인덱스
0 1 2 3 4
첫번째 1234랑 비교 -> 4
두번째 234 -> 3
세번째 34
네번째 4
마지막 -> 비교 x -> 0초

i는 비교 대상 -> 0, 1, 2, 3
'''
def get_price_not_fall_periods(prices):
    result = [0] * len(prices)
    for i in range(len(prices)-1):
        period = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                period += 1
            else:
                period += 1
                break
        result[i] = period
    return result
    


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))