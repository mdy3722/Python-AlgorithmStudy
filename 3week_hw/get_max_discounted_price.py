shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

'''
비싼 애에 높은 할인율 적용
가격 - 2개
쿠폰 - 3개
[a, b]
 0  1

배열.sort() // 오름차순 정렬
배열.sort(reverse=True) // 내림차순 정렬
'''
# 내 코드
# def get_max_discounted_price(prices, coupons):
#     original_sum = 0
#     discounted_sum = 0
#     prices.sort(reverse=True)
#     coupons.sort(reverse=True)

#     for price in prices:
#       original_sum += price

#     for i in range(len(prices)):
#       if i < len(coupons):
#         discounted_sum += (prices[i] * coupons[i] / 100)
    
#     return original_sum - discounted_sum

# 딩코님 코드
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0

    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
       discounted_price = prices[price_index] * (100 - coupons[coupon_index]) / 100
       max_discounted_price += discounted_price
       price_index += 1
       coupon_index += 1
    
    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))