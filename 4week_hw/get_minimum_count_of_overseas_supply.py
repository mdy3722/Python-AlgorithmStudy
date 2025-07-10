'''
라면 공장은 밀가루 하루에 1톤씩 사용
원래 공급받던 공장으로부터 k일 이후에야 밀가루 공급 받을 수 있음 -> 그전까지 해외 공장에서 밀가루를 수입해야
라면 공장은 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급 받고 싶다.
해외 공장은 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려줌

라면 공장에 남아있는 밀가루 수량 stock
밀가루 공급 일정 dates / 해당 시점에 공급 가능한 밀가루 수량 supplies
원래 공항으로부터 공급 받을 수 있는 시점 k
최소 몇 번 해외 공장으로부터 밀가루를 받는지 구하시오

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30

# 다음과 같이 입력값이 들어온다면,
# 현재 재고가 4개 있습니다. 그리고 정상적으로 돌아오는 날은 30일까지입니다.
# 즉, 26개의 공급량을 사와야 합니다!
# 그러면 제일 최소한으로 26개를 가져오려면? supplies 에서 20, 10 을 가져오면 되겠죠?
# 그래서 이 경우의 최소 공급 횟수는 2 입니다!

k - stock => 추가로 필요한 밀가루
stock까지는 버틸 수 있음
26개
dates = [4, 10, 15]
supplies = [20, 5, 10]

왜 힙이냐? 최대, 최소 선택 + stock 상황과 date에 따라 동적으로 상황이 변경됨
'''

import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    last_added_date_index = 0
    max_heap = []
    count = 0

    while stock <=k:   # stock이 k보다 크게 되면 멈춰도 된다.
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, supplies[last_added_date_index] * -1)
            last_added_date_index += 1
        
        heappop = heapq.heappop(max_heap)
        stock += (heappop * -1)
        count += 1

    return count
        



print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))